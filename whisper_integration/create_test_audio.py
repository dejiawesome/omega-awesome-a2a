# create_test_audio.py
import numpy as np
from scipy.io import wavfile

def create_test_audio():
    sample_rate = 16000
    duration = 2
    t = np.linspace(0, duration, int(sample_rate * duration))
    frequency = 440  # A4 note
    audio = np.sin(2 * np.pi * frequency * t)
    
    # Normalize
    audio = (audio * 32767).astype(np.int16)
    
    # Save
    wavfile.write('test_audio.wav', sample_rate, audio)

if __name__ == "__main__":
    create_test_audio()
