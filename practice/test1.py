import math
import uuid


def update_contact_ids():
    # Generate new UUIDs for ContactId and InitialContactId
    new_contact_id = str(uuid.uuid4())
    new_initial_contact_id = new_contact_id  # Assigning same value

    print("New ContactId:", new_contact_id)
    print("New InitialContactId:", new_initial_contact_id)

    # Optionally return the values if you need to use them elsewhere
    # return new_contact_id, new_initial_contact_id

update_contact_ids()


# weight =input('What is your weight? ')
# print(type(weight))
# kg = float(weight) * 0.435
# print(kg)
#
# x= 2.4
# print(math.ceil(x))
# print(math.floor(x))
# print(round(x))
