def printMikkoMasterShit(response):
    healthCareDistrict = input("Syötä haluamasi sairaanhoitopiiri:")
    while True:
        try:      
            x = str(response[healthCareDistrict]["tested"])
            break
        except:
            print("Syötteessä virhe!")
            healthCareDistrict = input("Syötä haluamasi sairaanhoitopiiri uudestaan:")

    print("Tested: " + str(response[healthCareDistrict]["tested"]))
    print("Population: " + str(response[healthCareDistrict]["population"]))
    print("Infected: " + str(response[healthCareDistrict]["infected"]))
    print("Tested pct: " + str((round(response[healthCareDistrict]["tested"]/response[healthCareDistrict]["population"],2))*100)+"%")
    print("infected pct: " + str(round(response[healthCareDistrict]["infected"]/response[healthCareDistrict]["population"],4)*100)+"%")
