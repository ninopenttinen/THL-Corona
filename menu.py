import requests
import json
import os
import numpy as np
from datetime import datetime
from hospital_cases import printHospitalCases
from infection_rates import printInfectionRates
from tested_cases import printTestedCases

url = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/processedThlData'
url2 = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/finnishCoronaHospitalData'
url3 = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/hcdTestData'
response = {}
response2 = {}
response3 = {}

# haetaan json-data tiedostosta jos tiedosto on alle päivän vanha
today = datetime.today()
modified_date_i = datetime.fromtimestamp(os.path.getmtime('./data_store/infection_rates.json'))
modified_date_h = datetime.fromtimestamp(os.path.getmtime('./data_store/hospital_cases.json'))
modified_date_t = datetime.fromtimestamp(os.path.getmtime('./data_store/tested_cases.json'))
duration_i = today - modified_date_i
duration_h = today - modified_date_h
duration_t = today - modified_date_t

# tallennetaan response json-tiedostoon, josta data on helpompi lukea
if duration_i.days > 1:
    try:
        response = requests.get(url).json() # requests muokkaa jsonin suoraan python objectiksi
        with open('./data_store/infection_rates.json','w') as i:
            json.dump(response, i)
            i.close()
        print("Infection rates data loaded from server successfully")
    except:
        print("Server not accessible")
else:
    with open('./data_store/infection_rates.json','r') as i:
        response = json.load(i)
        i.close()
    print("Infection rates data loaded from file successfully")

if duration_h.days > 1:
    try:
        response2 = requests.get(url2).json()
        with open('./data_store/hospital_cases.json','w') as h:
            json.dump(response2, h)
            h.close()
        print("Hospital cases data loaded from server successfully")
    except:
        print("Server not accessible")
else:
    with open('./data_store/hospital_cases.json','r') as h:
        response2 = json.load(h)
        h.close()
    print("Hospital cases data loaded from file successfully")

if duration_t.days > 1:
    try:
        response3 = requests.get(url3).json()
        with open('./data_store/tested_cases.json','w') as t:
            json.dump(response3, t)
            t.close()
        print("Tested cases data loaded from server successfully")
    except:
        print("Server not accessible")
else:
    with open('./data_store/tested_cases.json','r') as t:
        response3 = json.load(t)
        t.close()
    print("Tested cases data loaded from file successfully")

print("\n\
    **************************************\n\
    | Welcome to TAMK Corona application |\n\
    **************************************\n")

while True:
    select = 0

    while select not in ['1','2','3','4']:
        print("1. Show confirmed cases by healthcare district")
        print("2. Show hospital cases")
        print("3. Show tested cases by healthcare district")
        print("4. Quit")
        select = input()

    if int(select) == 1:
        for x in response['confirmed']:
            print(f"{x} ")

        healthCareDistrict = input("\nSelect healthcare district: ")

        select2 = 0
        while select2 != '1' and select2 != '2':
            print("1. Show full interval")
            print("2. Select interval")
            select2 = input()

        if int(select2) == 1:
            printInfectionRates(str(healthCareDistrict), "", response)

        elif int(select2) == 2:
            timeInterval = input("Select interval [MMDD-MMDD]: ")
            printInfectionRates(str(healthCareDistrict), timeInterval, response)
            

    elif int(select) == 2:
        nameOfHospital=[]

        for hospitalised in response2['hospitalised']:
            if(hospitalised['area'] not in nameOfHospital):
                nameOfHospital.append(hospitalised['area'])
            else:
                continue

        print(nameOfHospital)
        healthCareUnit = input("\nSelect hospital: ")
        
        if(healthCareUnit in nameOfHospital):
            print(healthCareUnit,"ok")

        select2 = 0
        while select2 != '1' and select2 != '2':
            print("1. Show full interval")
            print("2. Select interval")
            select2 = input()

        if int(select2) == 1:
            printHospitalCases(str(healthCareUnit), "", response2)


        elif int(select2) == 2:
            timeInterval2 = input("Select interval [MMDD-MMDD]: ")
            printHospitalCases(str(healthCareUnit), timeInterval2, response2)

    elif int(select) == 3:
        printTestedCases(response3)

    elif int(select) == 4:
        break

