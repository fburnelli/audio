import wave
import array

concatenated_audio = array.array('h')
 
for i in range(1, 11):
    with open(f'audio_chunk.bin', 'rb') as file:
        audio_chunk = file.read()
        audio_data = array.array('h', audio_chunk)
        concatenated_audio.extend(audio_data)

# Create a WAV file and store the concatenated audio data
with wave.open('output_concatenated.wav', 'w') as file:
    file.setnchannels(1)  # Mono
    file.setsampwidth(2)  # 2 bytes for linear16 encoding
    file.setframerate(16000)  # 16kHz sample rate
    file.setcomptype('NONE', 'not compressed')  # No compression
    file.writeframes(concatenated_audio)