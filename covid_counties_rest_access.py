import csv
import requests

url="https://github.com/nytimes/covid-19-data/blob/master/us-counties.csv?raw=true"

#nyt_counties=requests.get(url, stream=True)
nyt_counties=requests.get(url)

#s=open('us-counties.csv')
#counties=csv.reader(s)

nyt_counties.encoding='ISO-8859-1'
counties=csv.reader(nyt_counties.text.decode('ISO-8859-1').split('\n'))

header = counties.next()

for row in counties: 
   print (dict(zip(header,row)))




