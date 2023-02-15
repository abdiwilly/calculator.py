# this is a calculator pro

num1=eval(input("Enter first number:"))
num2=eval(input("Enter second number:"))

operator= input("enter operator:")
def add(num1,num2):
    result=num1 + num2
    print(result)

def subtract(num1,num2):
    result=num1 - num2
    print(result)

def multiply(num1,num2):
    result=num1 * num2
    print(result)

def divide(num1,num2):
    result=num1 / num2
    print(result)

if operator =="+":
    add(num1,num2)
elif operator=="-":
    subtract(num1,num2)
elif operator=="*":
    multiply(num1,num2)
elif operator=="/":
    divide(num1,num2)
elif operator=="x" or operator=="x":
    multiply(num1,num2)
