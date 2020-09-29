#!/usr/bin/python3

import csv
import requests

url="https://github.com/nytimes/covid-19-data/blob/master/us-counties.csv?raw=true"

nyt_counties=requests.get(url)

# The UTF-8 encoding from the source URL causes problems with Python 2, so we use Python 3.
#
# For more details, see: https://stackoverflow.com/a/14786752/1493790

counties=csv.reader(nyt_counties.text.split('\n'))

header = counties.__next__()

for row in counties: 
   print (dict(zip(header,row)))




