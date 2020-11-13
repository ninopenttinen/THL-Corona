def printInfectionRates(healthCareDistrict, interval, response):
    
    startDate = interval[0:4]
    endDate = interval[5:10]
    infections = []
    infectionsTotal = 0
    dates = []

    for hcd in response["confirmed"][f"{healthCareDistrict}"]:

        if startDate <= (hcd["date"][5:7] + hcd["date"][8:10]) <= endDate:
            infections.append(hcd["value"])
            dates.append(hcd["date"][5:7] + "/" + hcd["date"][8:10])

        elif interval == '':
            infections.append(hcd["value"])

    infectionsTotal = sum(infections)
    print(f"Total amount of infections in {healthCareDistrict}: {infectionsTotal}")
    """
    plt.plot(dates, infections)
    plt.ylabel('infections')
    plt.xlabel('date')
    plt.xticks([dates[0], dates[-1]], visible=True, rotation="horizontal")
    plt.show()
    """

