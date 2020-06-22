import requests
import json
from urllib.request import urlopen
d = "2019-09-25"

with urlopen('https://api.exchangeratesapi.io/' + d ) as response:
    source = response.read()

#print(source)
data = json.loads(source)

#print(len(data['rates']))

print(data['rates']['CAD'])
first = data['rates']['CAD']
d = "2020-05-14"
with urlopen('https://api.exchangeratesapi.io/' + d ) as response:
    source = response.read()

#print(source)
data = json.loads(source)

#print(len(data['rates']))

print(data['rates']['CAD'])
second = data['rates']['CAD']
answer = second - first
difp = 100 - (first * 100 / second) 
print(answer)
print(difp)