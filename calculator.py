import math

def calculator():
    x = float(input("First number: "))
    z = input("Operator: ")
    y = float(input("Second number: "))
    if x and y == float and z == "+":
        result = x + y
        print(result)
    elif z == "-":
        result = x - y
        print(result)
    elif z == "*":
        result = x * y
        print(result)
    elif z == "/":
        result = x / y
        print(result)
    else:
        print("Invalid operator")

if __name__ == "__main__":
    calculator()