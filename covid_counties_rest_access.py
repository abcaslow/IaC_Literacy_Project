#!/usr/bin/python3

import csv
import requests

url="https://github.com/nytimes/covid-19-data/blob/master/us-counties.csv?raw=true"

nyt_counties=requests.get(url)

counties=csv.reader(nyt_counties.text.split('\n'))

header = counties.__next__()

for row in counties: 
   print (dict(zip(header,row)))




