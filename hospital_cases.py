def printHospitalCases(hospital, timeframe, response):
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