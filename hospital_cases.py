from excel_import import importHospitalCases

def printHospitalCases(hospital, timeframe, response):
    # initialise the variables used later in the code
    totalHospitalised = 0
    inWard = 0
    inIcu = 0
    dead = 0
    totalHospitalised_list = []
    inWard_list = []
    inIcu_list = []
    dead_list = []
    dates = []
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
                totalHospitalised_list.append(totalHospitalised)
                inWard_list.append(inWard)
                inIcu_list.append(inIcu)
                dead_list.append(dead)
                dates.append(f'{queryDate[5:7]}/{queryDate[8:10]}')
            # if a specific timeframe is not given, print the latest result
            elif(timeframe == ""):
                totalHospitalised = hospital_q["totalHospitalised"]
                inWard = hospital_q["inWard"]
                inIcu = hospital_q["inIcu"]
                dead = hospital_q["dead"]
                totalHospitalised_list.append(totalHospitalised)
                inWard_list.append(inWard)
                inIcu_list.append(inIcu)
                dead_list.append(dead)
                dates.append(f'{queryDate[5:7]}/{queryDate[8:10]}')

    #print the result
    print("\nHospital: {}\nTotal hospitalised: {}\nWard: {}\nICU: {}\nDead: {}\n".format(hospital, totalHospitalised, inWard, inIcu, dead))
    importHospitalCases(totalHospitalised_list, inWard_list, inIcu_list, dead_list, dates, hospital)