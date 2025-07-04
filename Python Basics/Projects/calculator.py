from os import system
calculator = True

while calculator:
    symbol = input("Select a math operator. Type:\n'/' For DIVISION\n'*' for MULTIPLICATION\n'-' for SUBTRACTION\n'+' for ADDITION\n Your choice: ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if symbol == "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    elif symbol == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif symbol == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif symbol == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    else:
        print("Wrong input. TRY AGAIN.")
    
    calc_again = input("Would you like to do some calculations? (Y/N): ")

    if calc_again == "N":
        calculator = False
    system("cls")