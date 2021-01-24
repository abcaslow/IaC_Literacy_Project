#!/usr/bin/python3

import csv

f=open('CreditCard3.csv')
s=f.read()

#This converts the csv file into a Python list of strings.
mcap=csv.reader(s.split('\n'))

header = mcap.__next__()

# zip is a Python3 feature
x=[(dict(zip(header,row))) for row in mcap]

food_ent_flags=['UBER','PRIME','APPLE','CAFE','NETFLIX','WENDYS','CHIPOTLE','SPOTIFY','AMAZON']
total=0

#for i in (sorted(set([i['deviceIp'] for i in j['items']]))): print (i)


for i in x:
 if 'Date' in i and any([f in i['Description'] for f in food_ent_flags]):
  print ("{:15}{:40}{:15}".format(i['Date'],i['Description'],i['Debit']))
  total= total+float(i['Debit'])

print ("Total for food and entertainment: $",total)

finflags=['VENMO',' CHASE','LORD','WELLS','CAPITAL ONE']
total=0

print ("\n ========================================================= \n")

for i in x:
 if 'Date' in i and any([f in i['Description'] for f in finflags]):
  print ("{:15}{:40}{:15}".format(i['Date'],i['Description'],i['Debit']))
  total= total+float(i['Debit'])

print ("Total for finance and credit card balances $",total)


fixedpayments=['VERIZON','ALLY','ATT','FCWA','DOMINION','CUBESMART','ALLSTATE','TRAVELERS','EZPASS']
total=0

print ("\n ========================================================= \n")

for i in x:
 if 'Date' in i and any([f in i['Description'] for f in fixedpayments]):
  print ("{:15}{:40}{:15}".format(i['Date'],i['Description'],i['Debit']))
  total= total+float(i['Debit'])

print ("Total for finance and credit card balances $",total)

groceries=['GIANT','SAFEWAY']
total=0

print ("\n ========================================================= \n")

for i in x:
 if 'Date' in i and any([f in i['Description'] for f in groceries]):
  print ("{:15}{:40}{:15}".format(i['Date'],i['Description'],i['Debit']))
  total= total+float(i['Debit'])

print ("Total for groceries $",total)

travel=['AIRBNB','MARRIOTT','SPIRIT','BUDGET','UNITED','WESTIN','HOTEL']
total=0

print ("\n ========================================================= \n")

for i in x:
 if 'Date' in i and any([f in i['Description'] for f in travel]):
  print ("{:15}{:40}{:15}".format(i['Date'],i['Description'],i['Debit']))
  total= total+float(i['Debit'])

print ("Total for travel $",total)



