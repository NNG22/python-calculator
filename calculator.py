while True:
    print("Welcome to python caluclator")
    a=int(input("Enter you first number:-"))
    b=int(input("Enter you second number:-"))
    def add (a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b
    def modulo(a,b):
        return a%b
    def floor(a,b):
        return a//b
    print("Available options are add/subtract/divide/modulo/floor/multiply")
    chose_any_operation=input("Enter which operation you want to perform:-")
    if chose_any_operation=="add":
        print(add(a,b))
    elif chose_any_operation=="subtract":
        print(subtract(a,b))
    elif chose_any_operation=="divide":
        if b==0:
            print("denominator cant be zero")
        else:
            print(divide(a,b))
    elif chose_any_operation=="floor":
        print(floor(a,b))
    elif chose_any_operation=="multiply":
        print(multiply(a,b))
    else:
        
        print("Invalid operation please try again!!")
    perform_again=input("Do you wnat to perform again (Yes/No):-").lower()
    if perform_again!="yes":
        print("Thank you for using python caluclator")
        break