import sounddevice as sd
from scipy.io.wavfile import write

def record_audio():
    try:
        # 1. User Input
        duration = int(input("Enter duration of recording in seconds: "))

        # Constants
        sample_rate = 44100  # CD quality
        channels = 2         # Stereo

        # 4. User Feedback
        print("Recording will start now...")
        
        # 2. Recording
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
        sd.wait()  # Wait until recording is finished

        print("Recording finished. Saving file...")

        # 3. Saving the File
        write("out.wav", sample_rate, recording)

        print("Recording saved successfully as 'out.wav'.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the recorder
record_audio()
