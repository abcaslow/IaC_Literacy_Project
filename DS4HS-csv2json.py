#! /usr/bin/env python3

import json
import csv
import sys

f = open(sys.argv[1])

csv_reader = csv.reader(f)

headers = next(csv_reader)
json_data = [dict(zip(headers,row)) for row in csv_reader if len(row)>0]

print(json_data)
print (json.dumps(json_data, indent=4))

