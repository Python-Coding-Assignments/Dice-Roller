import random

def rollDie(diceRolls):
    """This function calculates the number of times a roll of two, seven, and twelve appeared."""

    #declarations and initializations of variables
    maxNumSides = 6
    dice1 = dice2 = 0
    rolls = {"2": 0, "7": 0, "12": 0}

    #for loop which runs the number of times the user requested to roll the die
    for i in range(0, diceRolls):
        #generating a random integer for each dice between the values one and six (inclusive)
        dice1 = random.randint(1, maxNumSides)
        dice2 = random.randint(1, maxNumSides)

        #conditional statement which increments the value of the key "2" by one
        if dice1 + dice2 == 2:
            rolls["2"] += 1
        #conditional statement which increments the value of the key "7" by one    
        elif dice1 + dice2 == 7:
            rolls["7"] += 1
        #conditional statement which increments the value of the key "12" by one    
        elif dice1 + dice2 == 12:
            rolls["12"] += 1

    #returning the local dictionary rolls
    return rolls                