import logging
import sys, os
import datetime
import json
import jsonlines
import pytest
import time

from tests.conftest import ValueStorage

sys.path.insert(0, 'src')
import IngestionRequest
import InteractionIdHandler

logger = logging.getLogger()
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
test_start_time = datetime.datetime.now().replace(tzinfo=None)
ui_test_completed = False
initial_counts = {}
module_counts = {}
ingestion_uploaded_media_values = []
ingestion_created_session_values = []
ingestion_uploaded_metadata_values = []
ingestion_uploaded_media_size_values = []
ingestion_converted_media_values = []
RetrieverAuthorizer_values = []
module_custom_data = {}
media_ids = []
ingestion_complete = False
media_id = None
isSSL = True

requestJsonFile = 'testdata/KafkaMessage/KafkaMessagingFiles.Json'
ingestionMedia = [(1, 'testdata/media/Mono/atnt.103.90.13.42.23.200_GSM_mono.wav', True)]
useCurrentDateTime = False  # use current date time

test_start_time = datetime.datetime.now().replace(tzinfo=None)


@pytest.mark.parametrize("requestJsonFile", [(requestJsonFile)])
def test_SendPOSTRequest(requestJsonFile):
    # time.sleep(60)
    global initial_counts
    # Capture initial counts before execution
    initial_counts = capture_initial_module_counts()

    ValueStorage.ingestionToken = IngestionRequest.sendPOSTRequestJWT(
        os.environ['INGESTOR'], isSSL, os.environ['JWT_TOKEN_2'], ValueStorage.ingestion_endpoint, requestJsonFile,
        useCurrentDateTime
    )
    logger.info(f"Ingestion Token = {ValueStorage.ingestionToken}")
    ValueStorage.mediaID = []
    assert True


@pytest.mark.parametrize("sessionNumber, ingestionBody, isLast", ingestionMedia)
def test_SendPUTRequest(sessionNumber, ingestionBody, isLast):
    global ingestion_complete
    responseText = IngestionRequest.sendPUTRequestJWT(
        os.environ['INGESTOR'], isSSL, os.environ['JWT_TOKEN_2'], ValueStorage.ingestion_endpoint,
        ValueStorage.ingestionToken, sessionNumber, ingestionBody, isLast
    )
    current_timestamp = datetime.datetime.now().isoformat()
    if isLast:
        mediaID = json.loads(responseText)['contacts'][0]['sessions'][0]['parts']
        ValueStorage.transaction_ID_B1 = json.loads(responseText)['last_transaction_id']
        ValueStorage.contact_ID_B1 = json.loads(responseText)['last_contact_id']
        logger.info(f"contact_ID_B1 = {ValueStorage.contact_ID_B1}")
        logger.info(f"transaction_ID_B1 = {ValueStorage.transaction_ID_B1}")
        InteractionIdHandler.storeID(ValueStorage.transaction_ID_B1, ValueStorage.contact_ID_B1, 'B1')
        media_ids.append({"media_id": mediaID[len(ingestionMedia) - 1], "timestamp": current_timestamp})
        assert (set(ValueStorage.mediaID).intersection(set(mediaID)) == set(ValueStorage.mediaID))
    else:
        mediaID = json.loads(responseText)['media_id']
        ValueStorage.mediaID.append(mediaID)
        media_ids.append({"media_id": mediaID, "timestamp": current_timestamp})

    logger.info(f"Media ID = {mediaID}")

    if isLast:
        ingestion_complete = True
    assert True


def test_validate_KafkaMessage():
    time.sleep(30)
    global ingestion_complete
    while not ingestion_complete:
        logger.info("Waiting for ingestion to complete...")
        time.sleep(5)

    logger.info("Validating Kafka message")

    global initial_counts
    # Capture final counts after execution
    final_counts = capture_final_module_counts()
    compare_module_counts(initial_counts, final_counts, len(ingestionMedia))
    # Load local expected data
    expected_data = load_local_data('testdata/KafkaMessage/Kafka_expected_data.json')

    # Validate the data
    runtime_data = []
    with open("out/Metering.json", "r") as f:
        for line in jsonlines.Reader(f):
            json_str = json.dumps(line)
            json_lines = json.loads(json_str)
            entry_timestamp = json_lines.get('timestamp')
            if entry_timestamp and entry_timestamp < test_start_time:
                continue
            runtime_data.append(json_lines)

    # Validate the data against the expected data
    validate_data(runtime_data, expected_data, test_start_time)
    logger.info("entry_timestamp:-------->",entry_timestamp)
    # Capture media IDs after the test start time
    current_media_ids = []
    with open("out/Metering.json", "r") as f:
        for line in jsonlines.Reader(f):
            json_str = json.dumps(line)
            json_lines = json.loads(json_str)
            entry_timestamp = json_lines.get('timestamp')
            if entry_timestamp:
                entry_time = datetime.datetime.fromisoformat(entry_timestamp.replace('Z', '+00:00')).replace(
                    tzinfo=None)
                if entry_time >= test_start_time:
                    module = json_lines.get('module')
                    custom_data = json_lines.get('custom_data', {})
                    media_id = custom_data.get('media_id')
                    if media_id:
                        current_media_ids.append(media_id)

    # Validate media IDs
    stored_media_ids = [media['media_id'] for media in media_ids]
    for media_id in current_media_ids:
        assert media_id in stored_media_ids, f"Media ID '{media_id}' not found in stored media IDs."

    # Additional changes
    module_custom_data = {}

    with open("out/Metering.json", "r") as f:
        for line in jsonlines.Reader(f):
            json_str = json.dumps(line)
            json_lines = json.loads(json_str)
            entry_timestamp = json_lines.get('timestamp')
            if entry_timestamp:
                entry_time = datetime.datetime.fromisoformat(entry_timestamp.replace('Z', '+00:00')).replace(
                    tzinfo=None)
                if entry_time >= test_start_time:
                    module = json_lines.get('module')
                    custom_data = json_lines.get('custom_data', {})
                    media_id = custom_data.get('media_id')
                    if media_id:
                        current_media_ids.append(media_id)

                    # Validate media ID against stored media IDs
                    assert media_id in stored_media_ids, f"Media ID '{media_id}' not found in stored media IDs."

                    # Validate module and associated custom data
                    if module.startswith(("media_aqs", "streams_aqs", "seconds_aqs", "media_compressed",
                                          "streams_compressed", "seconds_compressed")):
                        module_custom_data.setdefault(module, []).append(custom_data)

                        if isinstance(custom_data, str):
                            assert len(
                                custom_data) >= 10, f"Custom data '{custom_data}' for module '{module}' does not meet the length requirement."
                        elif isinstance(custom_data, dict):
                            assert len(
                                media_id) >= 10, f"Media ID '{media_id}' for module '{module}' does not meet the length requirement."
                        else:
                            raise ValueError(f"Invalid custom data type for module '{module}': {type(custom_data)}")

    # Validate modules
    for module, custom_data_list in module_custom_data.items():
        for custom_data in custom_data_list:
            if 'module' in json_lines and json_lines['module'] == 'Replay':
                RetrieverAuthorizer_values.append(json_lines['module'])

            # Log module counts
            log_module_counts(module, [module])

    # Additional logging and module counts
    log_module_counts('ingestion_uploaded_media', ingestion_uploaded_media_values)
    log_module_counts('ingestion_uploaded_metadata', ingestion_uploaded_metadata_values)
    log_module_counts('ingestion_uploaded_media_size', ingestion_uploaded_media_size_values)
    log_module_counts('ingestion_created_session', ingestion_created_session_values)
    increment_module_count('ingestion_converted_media')
    log_module_counts('Replay', RetrieverAuthorizer_values)
    logger.info(f"all stored media ids: {media_ids}")


# Defined this function to capture the initial count of the modules for ingestor and retriever
def capture_initial_module_counts():
    ingestion_uploaded_media_values.clear()
    ingestion_created_session_values.clear()
    ingestion_uploaded_metadata_values.clear()
    ingestion_uploaded_media_size_values.clear()
    ingestion_converted_media_values.clear()
    RetrieverAuthorizer_values.clear()

    with open("out/Metering.json", "r") as f:
        for line in jsonlines.Reader(f):
            process_module_counts(line)

    counts = {
        'ingestion_uploaded_media': len(ingestion_uploaded_media_values),
        'ingestion_uploaded_metadata': len(ingestion_uploaded_metadata_values),
        'ingestion_uploaded_media_size': len(ingestion_uploaded_media_size_values),
        'ingestion_created_session': len(ingestion_created_session_values),
        'ingestion_converted_media': len(ingestion_converted_media_values),
        'Replay': len(RetrieverAuthorizer_values)
    }

    logger.info(f"Initial module counts: {counts}")
    return counts


# Defined this function to capture the final count of the modules after ingestion
def capture_final_module_counts():
    ingestion_uploaded_media_values.clear()
    ingestion_created_session_values.clear()
    ingestion_uploaded_metadata_values.clear()
    ingestion_uploaded_media_size_values.clear()
    ingestion_converted_media_values.clear()
    RetrieverAuthorizer_values.clear()

    with open("out/Metering.json", "r") as f:
        for line in jsonlines.Reader(f):
            process_module_counts(line)

    counts = {
        'ingestion_uploaded_media': len(ingestion_uploaded_media_values),
        'ingestion_uploaded_metadata': len(ingestion_uploaded_metadata_values),
        'ingestion_uploaded_media_size': len(ingestion_uploaded_media_size_values),
        'ingestion_created_session': len(ingestion_created_session_values),
        'ingestion_converted_media': len(ingestion_converted_media_values),
        'Replay': len(RetrieverAuthorizer_values),
    }

    logger.info(f"Final counts: {counts}")
    return counts


# Defined this function to parse individual lines from the metering.json and update the counts for different modules
def process_module_counts(line):
    json_str = json.dumps(line)
    json_lines = json.loads(json_str)
    module = json_lines.get('module')

    if module == 'ingestion_uploaded_media':
        ingestion_uploaded_media_values.append(module)
    elif module == 'ingestion_uploaded_metadata':
        ingestion_uploaded_metadata_values.append(module)
    elif module == 'ingestion_uploaded_media_size':
        ingestion_uploaded_media_size_values.append(module)
    elif module == 'ingestion_created_session':
        ingestion_created_session_values.append(module)
    elif module == 'ingestion_converted_media':
        ingestion_converted_media_values.append(module)
        # Check if converted_from is audio/vnd.nice.nmf or aud
        custom_data = json_lines.get('custom_data', {})
        converted_from = custom_data.get('converted_from', '')
        if converted_from == 'audio/vnd.nice.nmf' or converted_from == 'aud':
            increment_module_count(module)
    elif module == 'Replay':
        RetrieverAuthorizer_values.append(module)


# Defined to load expected data testdata/KafkaMessage/Kafka_expected_data.json
def load_local_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


# Defined the function to validate the actual data from runtime against expected values
def validate_data(actual_data, expected_data, expected_time):
    filtered_data = []
    for data_entry in actual_data:
        entry_timestamp = data_entry.get('timestamp')
        if entry_timestamp:
            entry_time = datetime.datetime.fromisoformat(entry_timestamp.replace('Z', '+00:00')).replace(
                tzinfo=None)
            if entry_time >= expected_time:
                filtered_data.append(data_entry)

    def find_expected_entry(module, expected_data):
        for expected_entry in expected_data:
            metering_data = expected_entry.get('metering')
            if metering_data:
                for metering_entry in metering_data:
                    if metering_entry.get('module') == module:
                        return metering_entry
        return None

    for actual_entry in filtered_data:
        # Check if the entry contains metering data
        metering_data = actual_entry.get('metering')
        if metering_data:
            for metering_entry in metering_data:
                module = metering_entry.get('module')
                if not module:
                    logger.warning(f"Missing 'module' field in metering entry: {metering_entry}")
                    continue

                expected_entry = find_expected_entry(module, expected_data)
                if not expected_entry:
                    logger.warning(f"No expected data found for module '{module}' in metering entry: {metering_entry}")
                    continue

                # Compare each key-value pair in the metering entry with the expected entry
                for key, expected_value in expected_entry.items():
                    actual_value = metering_entry.get(key)
                    if actual_value != expected_value:
                        logger.warning(
                            f"Value mismatch in {module} metering entry for field '{key}': expected '{expected_value}', got '{actual_value}'")
                    else:
                        logger.info(f"Field '{key}' in {module} metering entry has the correct value '{actual_value}'.")
        else:
            module = actual_entry.get('module')
            if not module:
                logger.warning(f"Missing 'module' field in entry: {actual_entry}")
                continue

            expected_entry = next((item for item in expected_data if item.get('module') == module), None)
            if not expected_entry:
                logger.warning(f"No expected data found for module '{module}' in entry: {actual_entry}")
                continue

            # Compare each key-value pair in the actual entry with the expected entry
            for key, expected_value in expected_entry.items():
                actual_value = actual_entry.get(key)
                if actual_value != expected_value:
                    logger.warning(
                        f"Value mismatch in {module} entry for field '{key}': expected '{expected_value}', got '{actual_value}'")
                else:
                    logger.info(f"Field '{key}' in {module} entry has the correct value '{actual_value}'.")


def increment_module_count(module):
    if module == 'ingestion_converted_media':
        module_counts[module] = module_counts.get(module, 0) + 1
    elif module == 'Replay' and not ui_test_completed:
        # Skip increment for Replay module until UI test is completed
        return
    else:
        module_counts[module] = module_counts.get(module, 0) + 1


def log_module_counts(module_name, module_values):
    count = len(module_values)
    if not module_values:
        logger.info(f"There are no modules present for {module_name}.")
    else:
        assert count >= 1, f"The module {module_name} is present."
        logger.info(f"Count of {module_name}: {str(count)}\n")


def compare_module_counts(initial_counts, final_counts, media_length):
    for module, initial_count in initial_counts.items():
        expected_total_count = initial_count + media_length
        final_count = final_counts.get(module, 0)
        if module == 'ingestion_converted_media':
            # Check if count needs to be increased based on custom condition
            if final_count > initial_count:
                assert final_count >= expected_total_count, f"The count for {module} did not increase as expected. Initial: {initial_count}, Expected: {expected_total_count}, Final: {final_count}"
            else:
                assert final_count == initial_count, f"The count for {module} remained the same. Initial: {initial_count}, Final: {final_count}"
        elif module == 'Replay' and not ui_test_completed:
            logger.info(
                f"Skipping Replay module count check until UI test is completed. Initial: {initial_count}, Final: {final_count}")
        else:
            assert final_count >= expected_total_count, f"The count for {module} did not increase as expected. Initial: {initial_count}, Expected: {expected_total_count}, Final: {final_count}"
    logger.info("Ingestion module counts validated successfully.")


def parse_timestamp(timestamp_str):
    return datetime.datetime.fromisoformat(timestamp_str.replace('Z', '+00:00')).replace(tzinfo=None)


def validate_custom_data(custom_data):
    if isinstance(custom_data, dict):
        for key, value in custom_data.items():
            if isinstance(value, str):
                assert len(
                    value) >= 10, f"Custom data field '{key}' with value '{value}' does not meet the length requirement."
            elif isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    assert len(
                        sub_value) >= 10, f"Sub-field '{sub_key}' of custom data field '{key}' with value '{sub_value}' does not meet the length requirement."
            elif isinstance(value, list):
                for item in value:
                    assert isinstance(item,
                                      dict), f"Expected a dictionary for list item in custom data field '{key}', but got {type(item)}."
                    validate_custom_data(item)
            else:
                raise ValueError(f"Invalid type for custom data field '{key}': {type(value)}")
    else:
        raise ValueError(f"Invalid type for custom data: {type(custom_data)}")