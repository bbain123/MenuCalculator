#----------------------------------------------------
#Brendan Bain  251086487
# COMPSCI 1026A - 003
# Purpose: To take users order based off
# set menu, and compute the cost of the meal
#-----------------------------------------------------

doneOrderingMeal = False
doneOrderingQuantity = False
totalCost = 0
EGG = 0.99
BACON = 0.49
SAUSAGE = 1.49
HASH_BROWN = 1.19
TOAST = 0.79
COFFEE = 1.09
TEA = 0.89

# Method for handeling customer input with case and spaces
def formatInput(textLine) :
 textLine = textLine.lower().strip()
 wordList = textLine.split()
 textLine = " ".join(wordList)
 return textLine

#continues to loop as long as they are ordering
while not doneOrderingMeal:
    mealInput = input("Enter item (q to terminate): small breakfast, regular breakfast, big \n breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea:")
    tempCost = 0
    quantity = 0
    onMenu = True
    doneOrderingQuantity = False

#program checks whether user input is valid
    if formatInput(mealInput) == "small breakfast":
        tempCost = EGG + HASH_BROWN + 2.0*TOAST + 2.0*BACON + SAUSAGE

    elif formatInput(mealInput) == "regular breakfast":
        tempCost = 2.0*EGG + HASH_BROWN + 2.0*TOAST + 4.0*BACON + 2.0*SAUSAGE

    elif formatInput(mealInput) == "big breakfast":
        tempCost = 3.0*EGG + 2.0*HASH_BROWN + 4.0*TOAST + 6.0*BACON + 3.0*SAUSAGE

    elif formatInput(mealInput) == "egg":
        tempCost = EGG

    elif formatInput(mealInput) == "bacon":
        tempCost = BACON

    elif formatInput(mealInput) == "sausage":
        tempCost = SAUSAGE

    elif formatInput(mealInput) == "hash brown":
        tempCost = HASH_BROWN

    elif formatInput(mealInput) == "toast":
        tempCost = TOAST

    elif formatInput(mealInput) == "coffee":
        tempCost = COFFEE

    elif formatInput(mealInput) == "tea":
        tempCost = TEA

    elif formatInput(mealInput) == "q":
        doneOrderingMeal = True
        onMenu = False
    else:
        print("Please enter a valid option from the menu")
        onMenu = False

#doesnt let user continue if input entered isnt an int
    while onMenu and not doneOrderingQuantity:
        quantity = input("How many? : ")
        if quantity.isdecimal():
            doneOrderingQuantity = True

    totalCost += tempCost*float(quantity)         #calculates total cost

#prints cost of meal, tax, and final cost with tax
finalPrice = round(totalCost, 2)
print("\nCost :      $" , finalPrice)
print("Tax :       $", round(0.13*finalPrice, 2))
print ("Total :     $", (round((finalPrice + round(0.13*finalPrice, 2)),2)))
