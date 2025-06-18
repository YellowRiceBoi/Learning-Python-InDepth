import math

def calculator():
    x = input("First number: ")
    y = input("Second number: ")
    z = input("Operator: ")
    if z == "+":
        result = float(x) + float(y)
        print(result)
    elif z == "-":
        result = float(x) - float(y)
        print(result)
    elif z == "*":
        result = float(x) * float(y)
        print(result)
    elif z == "/":
        result = float(x) / float(y)
        print(result)

if __name__ == "__main__":
    calculator()