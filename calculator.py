# Simple Calculator - Python Project by Bhanu
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b if b!=0 else "Cannot divide by zero"

print("Simple Calculator - Built by Bhanu")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operator + - * / : ")

if op == '+':
    print("Result:", add(x,y))
elif op == '-':
    print("Result:", sub(x,y))
elif op == '*':
    print("Result:", mul(x,y))
elif op == '/':
    print("Result:", div(x,y))
else:
    print("Invalid operator")
