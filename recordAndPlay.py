import sounddevice as sd
import pyaudio
import numpy as np
# import soundfile as sf



#
# myrecording = np.asarray(data)

sd.default.samplerate = 48000
sd.default.channels = 2
duration = 5.5  # seconds
myrecording = sd.rec(int(duration * (sd.default.samplerate)), samplerate=sd.default.samplerate, channels=2)

# then playback
sd.wait()
sd.play(myrecording,sd.default.samplerate)
sd.wait()
# this is for playing from a particular file, needs soundfile import
# filename = "test.wav"
# data, fs = sf.read(filename, dtype='float32')
# sd.play(data, fs)
#
