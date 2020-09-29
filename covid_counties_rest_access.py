#!/usr/bin/python3

import csv
import requests

# The following url is the source of the covid cases by county data.
url="https://github.com/nytimes/covid-19-data/blob/master/us-counties.csv?raw=true"

#Run the play! this line actually intiates the HTTP get operation. 
nyt_counties=requests.get(url)

# The UTF-8 encoding from the source URL causes problems with Python 2, so we use Python 3.
#
# For more details, see: https://stackoverflow.com/a/14786752/1493790

#This converts the massive csv info received by the REST GET operation into a Python list of strings.
counties=csv.reader(nyt_counties.text.split('\n'))

header = counties.__next__()

for row in counties: 
   print (dict(zip(header,row)))




