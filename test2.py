import requests
import json
from urllib.request import urlopen

print("")
pd = input("Įveskite pirmąją datą: ")
ad = input("Įveskite antrąją datą: ")
val = input("Įveskite norimą valiutą: ")

with urlopen('https://api.exchangeratesapi.io/' + pd ) as response:
    source = response.read()

print(source)
data = json.loads(source)

#print(len(data['rates']))

print(pd, val, "valiutos kursas: ", data['rates'][val])
first = data['rates'][val]

with urlopen('https://api.exchangeratesapi.io/' + ad ) as response:
    source = response.read()

#print(source)
data = json.loads(source)

#print(len(data['rates']))

print(ad, val, "valiutos kursas: ", data['rates'][val])
second = data['rates'][val]
answer = first - second
difp = 100 - (second * 100 / first) 
print("Valiutos skirtumas: ", answer)
print("Valiutos skirtumas procentais: ", difp)