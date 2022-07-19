import json
import base64
import os


f = open("/Users/vikash/Desktop/data.json")

data = json.load(f)

decoded_bytes = base64.b64decode((data['result']['value']['data'][0]))

decoded_str = decoded_bytes.decode()
json_str = json.loads(decoded_str)
print(json_str)
