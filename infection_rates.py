from excel_import import importInfectionRates

def printInfectionRates(healthCareDistrict, interval, response):
    
    startDate = interval[0:4]
    endDate = interval[5:10]
    infections = []
    infectionsTotal = 0
    dates = []

    try:
        for hcd in response["confirmed"][f"{healthCareDistrict}"]:

            if startDate <= (hcd["date"][5:7] + hcd["date"][8:10]) <= endDate:
                infections.append(hcd["value"])
                dates.append(hcd["date"][5:7] + "/" + hcd["date"][8:10])

            elif interval == '':
                infections.append(hcd["value"])
                dates.append(hcd["date"][5:7] + "/" + hcd["date"][8:10])

        infectionsTotal = sum(infections)
        if interval == '':
            print(f"\nTotal amount of confirmed cases in {healthCareDistrict}: {infectionsTotal}\n")
            importInfectionRates(infections, dates, healthCareDistrict)
        else:
            print(f"\nTotal amount of confirmed cases between {dates[0]} - {dates[-1]} in {healthCareDistrict}: {infectionsTotal}\n")
            importInfectionRates(infections, dates, healthCareDistrict)

    except:
        print('\nInvalid healthcare district!\n')
