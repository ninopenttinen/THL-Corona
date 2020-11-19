def printTestedCases(response):
    
    for x in response:
        print(f"{x}")

    healthCareDistrict = input("\nSelect healthcare district: ")
    while True:
        try:      
            x = str(response[healthCareDistrict]["tested"])
            break
        except:
            print("Invalid input!")
            healthCareDistrict = input("Select healthcare district: ")

    print("\nTested: " + str(response[healthCareDistrict]["tested"]))
    print("Population: " + str(response[healthCareDistrict]["population"]))
    print("Infected: " + str(response[healthCareDistrict]["infected"]))
    print("Tested pct: " + str((round(response[healthCareDistrict]["tested"]/response[healthCareDistrict]["population"],2))*100)+"%")
    print("infected pct: " + str(round(response[healthCareDistrict]["infected"]/response[healthCareDistrict]["population"],4)*100)+"%\n")
