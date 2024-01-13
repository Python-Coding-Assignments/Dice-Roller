from Functions import menu, printResults, rollDie

#declarations and initializations of variables
value = False
numDiceRolls = 0
rolls = {}

#welcoming user to program
print("Welcome to the dice stats calculator!\nLet us know how many times to roll the dice!")
print("Enter 0 whenever you are ready to quit.\n")

#while loop which runs until the user enters the integer zero
while value == False:
    #getting a valid input for the number of times the user would like to roll the die
    numDiceRolls = menu()

    #conditional statement which runs if the user requests to roll the die zero times
    if numDiceRolls == 0:
        value = True
        continue

    #printing roll statistics    
    rolls = rollDie(numDiceRolls)
    printResults(numDiceRolls, rolls)
    
print("See ya!")