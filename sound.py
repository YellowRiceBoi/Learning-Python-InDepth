import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import numpy as np

# Sampling frequency
freq = 44100

# Recording duration
duration = 5

# Start recording with values
recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
sd.wait()

# Convert float64 array to int16
recording_int16 = np.int16(recording * 32767)

write("recording0.wav", freq, recording_int16)

# Convert the NumPy array to audio file
wv.write("recording1.wav", recording_int16, freq, sampwidth=2)

# Play the recorded audio
sd.play(recording_int16, freq)
sd.wait()  # Wait until the audio is finished playing
sd.stop()  # Stop the playback