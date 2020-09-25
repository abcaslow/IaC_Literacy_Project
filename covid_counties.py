import csv

s=open('new-york-times-source-us-counties.csv')
counties=csv.reader(s)

header = counties.next()

for row in counties: 
   print (dict(zip(header,row)))




