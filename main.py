import requests
from datetime import datetime, date, time
# Used source is from https://github.com/HS-Datadesk/koronavirus-avoindata
url = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/finnishCoronaHospitalData'

# import data from the API as JSON
response = requests.get(url).json()

# date format is assumed to be mmdd and year is 2020

# this function parses the data fetched in the line above.
# takes in parameters:
# hospital = desired hospital's data
# timeframe = desired timeframe
# prints the data fetched from the API with the set parameters limiting the scope of data shown
def printHospitalCases(hospital, timeframe):
    totalHospitalised = 0
    inWard = 0
    inIcu = 0
    dead = 0
    for hospital_q in response["hospitalised"]:
        if(hospital_q["area"] == hospital):
            totalHospitalised = hospital_q["totalHospitalised"]
            inWard = hospital_q["inWard"]
            inIcu = hospital_q["inIcu"]
            dead = hospital_q["dead"]
    print("\nHospital: {}\nTotal hospitalised: {}\nWard: {}\nICU: {}\nDead: {}\n".format(hospital, totalHospitalised, inWard, inIcu, dead))

# ask the user for the healthcare district and optional specific time period
printHospitalCases(input("Please select hospital by code (HYKS, KYS, OYS, TAYS, TYKS, Finland): ")
                  ,input("\nSelect start and end date in format (mmdd)-(mmdd). Year is assumed to be 2020\nEmpty query prints everything: "))

# optionally export to a CSV