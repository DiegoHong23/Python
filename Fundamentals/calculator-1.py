print("first number?")
number_1 = int(input())
print("second number?")
number_2 = int(input())
print("which operation?'*.+,-,/'")
operation = input()

def add_function():
    print(number_1 + number_2) 
def subtract_function():
    print(number_1 - number_2)
def multiply_function():
    print(number_1 * number_2)
def divide_function():
    print(number_1 / number_2)

if operation == "+":
    add_function()
elif operation == "-":
    subtract_function()
elif operation == "*":
    multiply_function()
elif operation == "/":
    divide_function()



