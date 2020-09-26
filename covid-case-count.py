import requests
import json

url = "https://api.covid19api.com/dayone/country/australia/status/confirmed"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

j=json.loads(response.text)

for i in j:
 if i['Province'].startswith("Ta"):
  print i['Date'], "   ", i['Province'], "   ", i["Cases"]

#print(response.text.encode('utf8'))
