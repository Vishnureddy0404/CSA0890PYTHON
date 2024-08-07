def get_input():
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number:"))
    return num1,num2
def perform_operations(num1,num2):
    while True:
        operation = input("enter operation(+,-,*,/,%,q to quit:)")
        if operation == "+":
            print(num1 + num2)
        elif operation == "-":
            print(num1 - num2)
        elif operation == "*":
            print(num1 * num2)
        elif operation == "/":
            if num2!=0:
                print(num1//num2)
            else:
                print("Error:Division by zero:")
        elif operation == "%":
            if num2!= 0:
                print(num1%num2)
            else:
                    print("Error:Division by Zero:")
        elif operation == "q":
            break
        else:
            print("Invalid operation.please try again.")
num1,num2 = get_input()
perform_operations(num1,num2)
