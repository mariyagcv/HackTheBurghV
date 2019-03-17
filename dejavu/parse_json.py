import json

with open('result.json') as f:
    data = json.load(f)
print(data['file_sha1'])
