from pydub import AudioSegment
import numpy as np
from scipy.spatial.distance import euclidean



def load_audio(file_path):
    return AudioSegment.from_file(file_path)

def get_chunks(audio, chunk_ms):
    return [audio[i:i+chunk_ms] for i in range(0, len(audio), chunk_ms)]

def audio_to_np(audio_chunk):
    samples = np.array(audio_chunk.get_array_of_samples())
    if audio_chunk.channels == 2:
        samples = samples.reshape((-1, 2))
        samples = samples.mean(axis=1)  # Convert to mono
    return samples

def test_compare_audio_chunks(file1, file2, chunk_ms=1000):
    audio1 = load_audio(file1)
    audio2 = load_audio(file2)

    chunks1 = get_chunks(audio1, chunk_ms)
    chunks2 = get_chunks(audio2, chunk_ms)

    min_len = min(len(chunks1), len(chunks2))
    distances = []

    for i in range(min_len):
        chunk1_np = audio_to_np(chunks1[i])
        chunk2_np = audio_to_np(chunks2[i])

        # Pad shorter chunk
        max_len = max(len(chunk1_np), len(chunk2_np))
        chunk1_np = np.pad(chunk1_np, (0, max_len - len(chunk1_np)))
        chunk2_np = np.pad(chunk2_np, (0, max_len - len(chunk2_np)))

        dist = euclidean(chunk1_np, chunk2_np)
        distances.append(dist)

    return distances

# Example usage
file1 = "C:\PythonPracticeProject\PyhtonPractice\practice\wav\Export_redacted_AC.wav"
file2 = "practice/wav/Redaction_Audio_Baseline_1.wav"
distances = test_compare_audio_chunks(file1, file2)
print("Chunk distances:", distances)
