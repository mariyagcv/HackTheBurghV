import sounddevice as sd
import pyaudio
import numpy as np
import time
# import soundfile as sf



#
# myrecording = np.asarray(data)
# create empty numpyarray myarray
# myrecording = record (same line)
# the while (record, some countdown)
# have play record
#
sd.default.samplerate = 48000
sd.default.channels = 2
duration = 0.01  # seconds
myRecording = sd.rec(int(duration * (sd.default.samplerate)), samplerate=sd.default.samplerate, channels=2)
# create a numpy here and initialise it to the copy of the first recording
myArray=np.array(myRecording, copy=True)
# myArray.zeros()
# print(myArray)
# then playback
countDown=7000    #equal to 7 seconds
# while(countDown>0):
sd.wait()
while 1:

    sd.play(myRecording,sd.default.samplerate)
    # time.sleep(0.03)
    myRecording=sd.rec(int(duration * (sd.default.samplerate)), samplerate=sd.default.samplerate, channels=2)
    sd.wait()
    myArray=np.append(myArray,myRecording,axis=0)
    # countDown=countDown-1

# myrecording = sd.playrec(myarray,sd.default.samplerate,channels=2)
# sd.wait()
# this is for playing from a particular file, needs soundfile import
# filename = "test.wav"
# data, fs = sf.read(filename, dtype='float32')
# sd.play(data, fs)
#
