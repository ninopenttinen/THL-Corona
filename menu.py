import requests
import matplotlib.pyplot as plt
from matplotlib import dates, pyplot
import numpy as np
from datetime import datetime
from hospital_cases import printHospitalCases
from infection_rates import printInfectionRates
from tested_cases import printMikkoMasterShit
import json
import os

url = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/processedThlData'
url2 = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/finnishCoronaHospitalData'
url3 = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/hcdTestData'
response = {}
response2 = {}
response3 = {}

if(os.path.exists('infection_rates.json') == False):
    i = open('infection_rates.json','x')
    i.close()

if(os.path.exists('hospital_cases.json') == False):
    h = open('hospital_cases.json','x')
    h.close()

if(os.path.exists('tested_cases.json') == False):
    t = open('tested_cases.json','x')
    t.close()

# haetaan json-data tiedostosta jos tiedosto on vähintään päivän vanha
today = datetime.today()
modified_date_i = datetime.fromtimestamp(os.path.getmtime('infection_rates.json'))
modified_date_h = datetime.fromtimestamp(os.path.getmtime('hospital_cases.json'))
modified_date_t = datetime.fromtimestamp(os.path.getmtime('tested_cases.json'))
duration_i = today - modified_date_i
duration_h = today - modified_date_h
duration_t = today - modified_date_t

# tallennetaan response json-tiedostoon, josta data on helpompi lukea
if duration_i.days > 1:
    try:
        response = requests.get(url).json() # requests muokkaa jsonin suoraan python objectiksi
        with open('infection_rates.json','w') as i:
            json.dump(response, i)
            i.close()
        print("Infection rates data loaded from server successfully")
    except:
        print("Server not accessible")
else:
    with open('infection_rates.json','r') as i:
        response = json.load(i)
        i.close()
    print("Infection rates data loaded from file successfully")

if duration_h.days > 1:
    try:
        response2 = requests.get(url2).json()
        with open('hospital_cases.json','w') as h:
            json.dump(response2, h)
            h.close()
        print("Hospital cases data loaded from server successfully")
    except:
        print("Server not accessible")
else:
    with open('hospital_cases.json','r') as h:
        response2 = json.load(h)
        h.close()
    print("Hospital cases data loaded from file successfully")

if duration_t.days > 1:
    try:
        response3 = requests.get(url3).json()
        with open('tested_cases.json','w') as t:
            json.dump(response3, t)
            t.close()
        print("Tested cases data loaded from server successfully")
    except:
        print("Server not accessible")
else:
    with open('tested_cases.json','r') as t:
        response3 = json.load(t)
        t.close()
    print("Tested cases data loaded from file successfully")

print("\n    ****************************************\n\
    | Tervetuloa Tamkin koronasovellukseen |\n\
    ****************************************\n")

while True:
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

