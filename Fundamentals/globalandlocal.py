print("first number?")
number_1 = int(input())
print("second number?")
number_2 = int(input())
print("which operation?'*.+,-,/'")
operation = input()

# number_1 and number_2 and operation are global variables 

def add_function():
    x = 10
    print(number_1 + number_2) 
def subtract_function():
    print(number_1 - number_2)
def multiply_function():
    print(number_1 * number_2)
def divide_function():
    print(number_1 / number_2)

# print(x)    # x is local variable in add_function, x is only valid in add_function scope

if operation == "+":
    y = 10
    add_function()
elif operation == "-":
    subtract_function()
elif operation == "*":
    multiply_function()
elif operation == "/":
    divide_function()

print(y) # y is a local variable within the if statement, y is only valid inside the if statement.