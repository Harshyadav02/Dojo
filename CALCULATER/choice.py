from Calculater import *

def takechoice():
    var = input("enter y or n ").lower()
    if var == "y":
        
        return True
    elif var == "n":
       
        return False
    else:
        print("Enter valid choice ")
        takechoice()
test = True

while True:
    if test == True :
        calc()
        test = takechoice()

    else:
        print("Thanks for using the cal ")
        break
