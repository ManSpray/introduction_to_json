import requests
import json
from urllib.request import urlopen

failas = open("valiutos.txt", "r")
#print(failas.readable())
#print(failas.read())
pd = failas.readline() #input("Įveskite pirmąją datą: ")
ad = failas.readline() # input("Įveskite antrąją datą: ")
val = failas.readline() # input("Įveskite norimą valiutą: ")
failas.close()

with urlopen('https://api.exchangeratesapi.io/' + pd ) as response:
    source = response.read()

#print(source)
data = json.loads(source)

#print(len(data['rates']))
ats1 = str (data['rates'][val])
rez = open("rezultatai.txt", "w")
rez.write(pd)
rez.write('Valiutos kursas:   ')
rez.write(ats1)
rez.write('\n')
#print(pd, val, "valiutos kursas: ", data['rates'][val])
first = data['rates'][val]

with urlopen('https://api.exchangeratesapi.io/' + ad ) as response:
    source = response.read()

#print(source)
data = json.loads(source)

#print(len(data['rates']))
rez.write(ad)
rez.write('Valiutos kursas:  ')
ats2 = str (data['rates'][val])
rez.write(ats2)
rez.write('\n')
print(ad, val, "valiutos kursas: ", data['rates'][val])
second = data['rates'][val]
answer = str (first - second)
difp = str (100 - (second * 100 / first))
rez.write("Valiutos skirtumas:   ")
rez.write(answer)
rez.write('\nValiutos skirtumas procentais:  ')
rez.write(difp)
rez.write('\n')
rez.close()
#print("Valiutos skirtumas: ", answer)
#print("Valiutos skirtumas procentais: ", difp)