# import pyaudio
#
# p = pyaudio.PyAudio()
#
# stream = p.open(format=pyaudio.paFloat32,
#                 channels=1,
#                 rate=44100,
#                 output=True)
#
# data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
#
# while data != '':
#     stream.write(data)
#     data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
#
# stream.stop_stream()
# stream.close()
#
# p.terminate()

import pyaudio

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 15

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("* recording")

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    stream.write(data, CHUNK)

print("* done")

stream.stop_stream()
stream.close()

p.terminate()
