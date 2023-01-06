import Type_check  as ui
import final as f

### operations to be performed

def calc():
    user_input1= input("enter the  first Numeric value you wanna perform operation: ")
    user_input2= input("enter the  second Numeric value you wanna perform operation: ")
    
    ### checking the given input by user wheater it is Int or Float
    user_input1 = ui.check(user_input1)
    print(type(user_input1))

    user_input2 = ui.check(user_input2)
    print(type(user_input2))

    print()

    def add(x,y):
        z = x+y
        print(z)
        
    def sub(x,y):
        z = x-y
        print(z) 
        
    def mul(x,y):
        z = x*y
        print(z)
    def div(x,y):
        if user_input2 == 0:
            print("cannot operater ")
        else:    
            z = x/y
            c = f.con(z)
            print(c)
    def mod(x,y):
        z = x%y
        print(z)
    def power(x,y):
        z = x**y
        print(z)
    ### user choice 
   
    print()
    print(""" press the operation you Wanna perfor
                +       -
                *       / 
                %        **

    """)
    
    choice = input("enter your choice: ")
    if choice == '+':
        add(user_input1,user_input2)
        
    elif choice == "-":
        sub(user_input1,user_input2)
        
    elif choice == "*":
        mul(user_input1,user_input2)
    
    elif choice == "/":
        div(user_input1,user_input2)
    elif choice == "%":
        mod(user_input1,user_input2)
    elif choice == "**":
        power(user_input1,user_input2)
    else:
        print("invalid choice")   



'''def takechoice():
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
'''

