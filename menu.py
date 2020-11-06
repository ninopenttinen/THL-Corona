import requests
import matplotlib.pyplot as plt
from matplotlib import dates, pyplot
import numpy as np
from datetime import datetime
from hospital_cases import printHospitalCases
from infection_rates import printInfectionRates

url = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/processedThlData'
url2 = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/finnishCoronaHospitalData'
response = requests.get(url).json() # requests muokkaa jsonin suoraan python objectiksi
response2 = requests.get(url2).json()

print("                                    ")
print("****************************************")
print("| Tervetuloa Tamkin koronasovellukseen |")
print("****************************************")
print("                                    ")

select = 0

#char?+
while int(select) != 1 and int(select) != 2:
    print("1. Valitse tapauksen sairaanhoitopiireittäin")
    print("2. Valitse tapaukset sairaaloittain")
    select  = input()

#ilman f ei voi upottaa parametrejä / f string

nameOfDistrict=[]

if int(select) == 1:
    for x in response['confirmed']:
        nameOfDistrict.append(x)
        print(f"{x} ")

    healthCareDistrict = input("Syötä haluamasi sairaanhoitopiiri: ")

    select2 = 0
    while int(select2) != 1 and int(select2) != 2:
        print("1. Näytä koko aikaväli ")
        print("2. Valitse aikaväli ")
        select2 = input()

    if int(select2) == 1:
        printInfectionRates(str(healthCareDistrict), "", response)

    elif int(select2) == 2:
        timeInterval = input("Valitse aikaväli muodossa KKPP-KKPP: ")
        printInfectionRates(str(healthCareDistrict), timeInterval, response)
        

elif int(select) == 2:

    nameOfHospital=[]

    for hospitalised in response2['hospitalised']:
        if(hospitalised['area'] not in nameOfHospital):  #not in
            nameOfHospital.append(hospitalised['area'])
        else:
            continue

    print(nameOfHospital)    

    healthCareUnit = input("Syötä haluamasi sairaala: ")

    if(healthCareUnit in nameOfHospital):
        print(healthCareUnit,"ok")
    
    select2 = 0
    while int(select2) != 1 and int(select2) != 2:
        print("1. Näytä koko aikaväli ")
        print("2. Valitse aikaväli ")
        select2 = input()

    if int(select2) == 1:
        printHospitalCases(str(healthCareUnit), "", response2)


    elif int(select2) == 2:
        timeInterval2 = input("Valitse aikaväli muodossa KKPP-KKPP: ")
        printHospitalCases(str(healthCareUnit), timeInterval2, response2)

