import math

while True :
    num1 = int(input("Enter frist number: "))
    operator = input("Select the operators(+,-,*,/,**): ")
    num2 =int(input("Enter the second number: "))

    if operator == "+": 
        sum = num1 + num2
        print("addition = "+str(sum))
    elif operator == "-":
        sub = num1 - num2
        print("substraction = "+str(sub))
    elif operator == "*":
        prod = num1 * num2
        print("Multiplication = "+str(prod))
    elif operator == "/":
        div = num1 / num2
        print("Division = "+str(div))
    elif operator == "**":
        pow = num1**num2
        print("Power = "+str(pow))
    else :
        print("Please Enter the valid operator")

    again = input("If you want to continue plz enter yes\nElse enter any word and press enter to exit = ").lower()

    if again != "yes":
        break;

