import subprocess
record = 'arecord -d 5 test.wav'
p = subprocess.Popen(record, shell=True)
