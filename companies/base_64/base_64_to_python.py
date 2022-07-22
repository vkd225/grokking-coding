import base64
import json
import os
from pprint import pprint

directory = os.listdir('/Users/vikash/Desktop/grokking_the_coding_interview/companies/base_64')
os.chdir('/Users/vikash/Desktop/grokking_the_coding_interview/companies/base_64')
data={}

for file in directory:
  base = os.path.basename(file)
  data["label"] = base
  open_file = open(file,'rb')
  image_read = open_file.read()
  image_64_encode = base64.encodebytes(image_read)
  data["data"] = image_64_encode.decode('ascii')
  final_data = json.dumps(data)
  # make_file.write(final_data)

print (data)


