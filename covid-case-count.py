import requests
import json
import sys

x=sys.argv[1]

def genius(**kwarg):
 print kwarg
 global popprovince
 popprovince=kwarg

genius(New=8100000,Vic=6700000, Tas=540000)

url = "https://api.covid19api.com/dayone/country/australia/status/confirmed"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

j=json.loads(response.text)

for i in j:
 if i['Province'].startswith(x):
  covidinpop = (float(i['Cases'])/popprovince[x])*100
  print i['Date'], "   ", i['Province'], "   ", i["Cases"], "  ", "{:5.2f} %".format(covidinpop)

