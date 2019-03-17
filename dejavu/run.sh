#!/bin/bash
if [ -z "$1" ]
  then
    arecord my_recording.wav --rate=44100 -f cd --buffer-size=1024 -d 30
  else 
    arecord my_recording.wav --rate=44100 -f cd --buffer-size=1024 -d $1
fi
python dejavu.py --recognize file my_recording.wav &> result.json
sshpass -p $(python parse_json.py result.json)  ssh -o StrictHostKeyChecking=no mihai@10.42.0.121


