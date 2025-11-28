def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
while True:
    try:
        a = int(input("Enter 1st Number : "))
        b = int(input("Enter 2nd NUmber : "))
    except:
        print("Give valid Inputs.")
    func = input("Enter Operation : \n 1-Addition\n 2-Subtraction\n 3-Multiplication\n 4-Division\n Anything For Exit.\n ")
    if func == '1':
        print(f"The Addition of {a} and {b} is - {add(a,b)}")
    elif func == '2':
        print(f"The Subtraction of {a} and {b} is -  {subtract(a,b)}")
    elif func == '3':
        print(f"The Multiplication of {a} and {b} is -  {multiply(a,b)}")
    elif func == '4':
        print(f"The Division of {a} and {b} is -  {divide(a,b)}")
    else:
        print("Thank You For Using Us.Exiting.😊")
        break
