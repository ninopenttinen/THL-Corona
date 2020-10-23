import requests
from datetime import datetime, date, time
# Used source is from https://github.com/HS-Datadesk/koronavirus-avoindata
url = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/processedThlData'

# import data from the API as JSON
response = requests.get(url).json()
for date in range(100,250):
    print(response["confirmed"]["Ahvenanmaa"][date])

# parse JSON and divide data into a list or dictionary
# print list or dictionary visually with matplotlib
# optionally ask the user for the healthcare district
# optionally ask the user for a specific time period
# optionally export to a CSV