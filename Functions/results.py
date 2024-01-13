def printResults(totalRolls, dieRolls):
    """This function will some statistics that were observed by rolling the die."""

    #printing number of times a roll of two appeared
    print("\nResults:\nA roll of 2 appeared " + str(dieRolls["2"]) + " total times, ", end= "")
    print(str("{:.2f}".format((dieRolls["2"] / totalRolls) * 100)) + "% of the time.")

    #printing the number of times a roll of seven appeared
    print("A roll of 7 appeared " + str(dieRolls["7"]) + " total times, ", end= "")
    print(str("{:.2f}".format((dieRolls["7"] / totalRolls) * 100)) + "% of the time.")

    #printing the number of times a roll of twelve appeared
    print("A roll of 12 appeared " + str(dieRolls["12"]) + " total times, ", end= "")
    print(str("{:.2f}".format((dieRolls["12"] / totalRolls) * 100)) + "% of the time.\n")