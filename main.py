# DEPRECATED AND MOVED TO HOSPITAL_CASES.PY

# dependencies
import requests
import matplotlib.pyplot as plt
from matplotlib import dates, pyplot
import numpy as np
from datetime import datetime

# date format is assumed to be mmdd and year is 2020

# this function parses the data fetched in the line above.
# takes in parameters:
# hospital = desired hospital's data
# timeframe = desired timeframe
# prints the data fetched from the API with the set parameters limiting the scope of data shown

def printHospitalCases(hospital, timeframe):
    # initialise the variables used later in the code
    totalHospitalised = 0
    inWard = 0
    inIcu = 0
    dead = 0
    # check if a specific timeframe is given and create string variables to limit the search with
    if(timeframe != ""):
        startQuery = "2020-{}{}-{}{}{}".format(timeframe[0], timeframe[1], timeframe[2], timeframe[3], "T13:00:00.000Z")
        endQuery = "2020-{}{}-{}{}{}".format(timeframe[5], timeframe[6], timeframe[7], timeframe[8], "T13:00:00.000Z")

    # search through the response
    for hospital_q in response["hospitalised"]:
        queryDate = hospital_q["date"]
        if(hospital_q["area"] == hospital):
            # if a specific timeframe is given, it is checked for here
            if(timeframe != "" and queryDate >= startQuery and queryDate <= endQuery):
                totalHospitalised = hospital_q["totalHospitalised"]
                inWard = hospital_q["inWard"]
                inIcu = hospital_q["inIcu"]
                dead = hospital_q["dead"]
            # if a specific timeframe is not given, print the latest result
            elif(timeframe == ""):
                totalHospitalised = hospital_q["totalHospitalised"]
                inWard = hospital_q["inWard"]
                inIcu = hospital_q["inIcu"]
                dead = hospital_q["dead"]
                
    #print the result
    print("\nHospital: {}\nTotal hospitalised: {}\nWard: {}\nICU: {}\nDead: {}\n".format(hospital, totalHospitalised, inWard, inIcu, dead))

def dialog():
    cont = True
    while(cont):
        # ask the user for the healthcare district and optional specific time period
        printHospitalCases(input("Please select hospital by code (HYKS, KYS, OYS, TAYS, TYKS, Finland): ")
                        ,input("\nSelect start and end date in format (mmdd)-(mmdd) without parentheses. Year is assumed to be 2020\nEmpty query prints everything: "))
        if(input("Continue? Y/N: ") == 'N'):
            cont = False

# Used source is from https://github.com/HS-Datadesk/koronavirus-avoindata
url = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/finnishCoronaHospitalData'

# import data from the API as JSON
response = requests.get(url).json()

# runtime
dialog()

# optionally export to a CSV