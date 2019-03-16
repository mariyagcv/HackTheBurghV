import pyaudio
import numpy as np
import sounddevice as sd

CHUNK = 4096 # number of data points to read at a time
RATE = 44100 # time resolution of the recording device (Hz)


sd.default.samplerate = 48000
sd.default.channels = 2

p=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input device

# create a numpy array holding a single read of audio data
for i in range(50): #to it a few times just to see
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    print(data)
    sd.play(data,sd.default.samplerate)
    sd.wait()

# close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()
