def menu():
    """This function takes in no arguments and simply prints a display and prompts the user the enter an integer value for the number of times the die should be rolled.  The function then returns that input, the number of rolls."""

    #declaration and initialization of variable
    numOfRolls = -1

    #while loop which runs until the user enters an integer value that is greater than or equal to zero
    while numOfRolls < 0:
        #prompting user to enter the number of times the die should be rolled
        print("How many times should we roll the dice?")
        numOfRolls = int(input("> "))

        #conditional statement which will print the following message if the number of times the die are rolled is greater than zero
        if numOfRolls > 0:
            print("Rolling dice " + str(numOfRolls) + " times...")
        #conditional statement which will print the following message if the number of times the die are rolled is less than zero    
        elif numOfRolls < 0:
            print("Cannot roll the die a negative number of times")
    #return the variable numOfRolls
    return numOfRolls