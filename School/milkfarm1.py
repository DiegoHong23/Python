# Milk Farm 20/1/23

# array = 1, 2, 4   , Same data type
# list = 1, '2', {},  mixed data type

# Option 1: Dictionary in List
# cows = [
#     {123: [0,9,0,0,0,0,0]},
# ]

# # Option 2: two list
# cows = [123, 345],
# milks =[
#     [0,9,0,0,0,0,0],     # index = 0, milks[0][1]
#     [0,0,0,0,0,0,0]      
# ]

cows = []
milk_amount = []
while True:
    print('cow id?')
    cow = input()
    if cow == '': 
        break
    if cow in cows:
        print('invalid - not unique')
        continue 
    if len(cow) == 3:
        print('valid')
    else:
        print('invalid wrong amount of digits')
        continue
    cows.append(cow)
    milk_amount.append(0)
    print(cows)
    print(milk_amount)

# Milking 
# cows = [123,234,345]
milk = [0,0,0]
while True:
    c = input('cow id?')
    if c =='':
        break
    i = 0
    while True:
        print(cows[i])
        if c==cows[i]:
            print('found it')
            break
        i += 1
    m = int(input('How much?'))
    milk[i]=m 

# Maximum amount is the cow that has produced the most milk in a week (Cow 123 with, 55, litres of milk has produced the most milk in a week)
# Minimum amount is the cow that has produced the least amount of milk in a week(Cow 234 with, 26, litres of milk has produced the least amount of milk in a week)
# Average amount is the average amount of milk produced by all cows in a week (The average amount of milk between each cow is, 34)
# Total is the total amount of milk produced by every cow in a week. (The total amount of milk produced by every cow is, 150)

