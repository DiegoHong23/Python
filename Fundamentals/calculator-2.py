print("first number?")
number_1 = int(input())
print("second number?")
number_2 = int(input())
print("which operation?'*.+,-,/'")
operation = input()

def add_function(num_1,num_2):
    print(num_1 + num_2)

def subtract_function(number_1,number_2):
    print(number_1 - number_2)

def multiply_function(number_1,number_2):
    print(number_1 * number_2)

def divide_function(number_1,number_2):
    print(number_1 / number_2)

# print(x)    # x is local variable in add_function, x is only valid in add_function scope

if operation == "+":
    add_function(num_1=number_1, num_2=number_2)
elif operation == "-":
    subtract_function(number_1,number_2)
elif operation == "*":
    multiply_function(number_1,number_2)
elif operation == "/":
    divide_function(number_1,number_2)

