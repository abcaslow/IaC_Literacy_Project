#!/usr/bin/python3

import csv

f=open('market-cap11.csv')
s=f.read()

#This converts the csv file into a Python list of strings.
mcap=csv.reader(s.split('\n'))

header = mcap.__next__()

# zip is a Python3 feature
x=[(dict(zip(header,row))) for row in mcap]

for i in x:
 print ("{:5}{:25}{:20}{:15}".format(i['rank'],i['company'],i['market-cap'],i['date']))
 




