import requests
import json


url = "https://api.covid19api.com/summary"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

#print(response.text.encode('utf8'))


payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

#print(response.text.encode('utf8'))
j= json.loads(response.text)
for i in j['Countries']:
#  if i['Country'].startswith('Sw') or i['Country'].startswith('Ir'):
#  if i['CountryCode'].startswith('U') and i['NewConfirmed'] >10:
  if i['NewConfirmed'] >5000:
#  if i['NewConfirmed'] <10:
   print i['Country'], "   ", i['NewConfirmed']


