#!/usr/bin/python3

import csv
import sys

f=open('market-cap50.csv')
s=f.read()

try: 
 sector=sys.argv[1]
except IndexError:
 pass


#This converts the csv file into a Python list of strings.
mcap=csv.reader(s.split('\n'))

header = mcap.__next__()

# zip is a Python3 feature
x=[(dict(zip(header,row))) for row in mcap]
#x={k:v for (k,v) in x.items() if
x=[i for i in x if sector in i['sector']]

for i in x: i['market-cap-int']=(float(i['market-cap'].replace(',','')))

xx=sum([i['market-cap-int'] for i in x])

xx_half=xx/2

i=x.__iter__()

lst=[]

while xx_half > 0:
 n=i.__next__()
 lst.append(n)
 xx_half=xx_half-n['market-cap-int']

len(lst)

for i in x:
 print ("{:5}{:25}{:25}{:15}{:12}{:15}".format(i['rank'],i['company'],i['market-cap'],i['sector'],i['ipo-date'],i['date']))

print ("========================================================")

print ('the top', len(lst), 'companies equal the bottom', len(x)-len(lst), 'companies')
 




