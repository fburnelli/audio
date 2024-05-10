import wave

DATA_FOLDER = "../../data/audio"
AUDIO_FILE = "conv_id_9a548943-8587-431b-aed5-6995a61a7be1.wav"

full_path = f"{DATA_FOLDER}/{AUDIO_FILE}"
try:
    with wave.open(full_path, 'rb') as wav_file:
        # Print basic properties of the WAV file
        print("Number of channels:", wav_file.getnchannels())
        print("Sample width (bytes) NOTE this relates to dynamic range:", wav_file.getsampwidth())
        print("Frame rate (sample rate, Hz):", wav_file.getframerate())
        print("Number of frames:", wav_file.getnframes())
        print("Compression type:", wav_file.getcomptype())
        print("Compression name:", wav_file.getcompname())
        print("params:", wav_file.getparams())

        ###read the frames
        frames = wav_file.readframes(-1)        
        print(frames)

except FileNotFoundError:
    print(f"The file {full_path} does not exist.")
except wave.Error as e:
    print(f"Could not read the WAV file: {e}")




### to write a file use the setter insteda of getterf