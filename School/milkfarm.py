# Milk Production 20/1/23 
identity = []
milk_amount = []
DAYS = 7
# Finding how many cows
while True: 
    print("How many cows?")
    cows = input()
    try: 
        cows = int(cows)
        break
    except: 
        ("Please input numbers")
        continue
  
# Asking for cow id
for codes in range(cows):
    while True:
        print("Please input 3 digit identity code")
        code = input()
        try: 
            code = int(code)
        except: 
            print("Please input numbers")
            continue
        if len(str(code)) == 3: 
            print("valid amount")
        else: 
            print('number of digits incorrect')
            continue
        if code in identity:
            print("Invalid - but already exists")
            continue
        else:
            print("Accepted codes")
            break
    identity.append(code)
# Milking inputs
# for index in range(cows): 
#     for j in range():
#         while True:
#             print("How much milk produced by", identity[index])
#             milk = input()
#             try:
#                 milk = int(milk)
#                 milk_amount.append(milk)
#                 break
#             except: 
#                 print("Please input numbers")
#                 continue

for index in range(cows):
    milks = []
    for j in range(DAYS): 
        print("How much milk produced by", identity[index],"in day", j+1)
        milk = input()
        try:
            milk = int(milk)
        except:
            print("Invalid - please input numbers")
        milks.append(milk)
    milk_amount.append(milks)
print(milk_amount)


# Finding cow that has produced the most milk in a week
max_milk = -1
cow = 0 
for index in range(len(milk_amount)):
    total_milk_amount = 0
    for j in range(len(milk_amount[index])):
        total_milk_amount = total_milk_amount + milk_amount[index][j]
    # print(total_milk_amount)
    if total_milk_amount>max_milk:
        max_milk=total_milk_amount
        cow=identity[index]

# print(milk_amount[index])
print('cow', cow, 'has produced the maximum amount of milk with', max_milk, 'litres of milk' )
# print('the total milk amoount is', total_milk_amount)

# Finding the cow that has produced the least milk in a week 
min_milk = 1000000000000
cow = 0 
for index in range(len(milk_amount)):
    total_milk_amount = 0
    for j in range(len(milk_amount[index])):
        total_milk_amount = total_milk_amount + milk_amount[index][j]
    # print(total_milk_amount)
    if total_milk_amount<min_milk:
        min_milk=total_milk_amount
        cow=identity[index]

print('cow', cow, 'has produced the minimum amount of milk with', min_milk, 'litres of milk' )

# Finding the total amount of milk produced in a week 
total_milk_amount1 = 0
for index in range(len(milk_amount)):
    for j in range(len(milk_amount[index])):
        total_milk_amount1 = total_milk_amount1 + milk_amount[index][j]
print('Total amount of milk produced is',total_milk_amount1)
# Finding the average amount of milk produced in a week 
average_milk = total_milk_amount1 / DAYS
print('The average of milk produced in a week is ', average_milk,'litres of milk')
    # max_milk = -1
# cow = 0
# for index in range(len(milks)):
#     if milks[index]>max_milk:
#         max_milk=milks[index]
#         cow=cows[index]
# print(index)
        

# for i in range(len(cows_milks)):
#     for j in range(len(cows_milks[i])):
#         print(cows_milks[i][j])

# print("Cows = ", identity)
# print("Milk Yields =", milk_amount)


# Maximum amount is the cow that has produced the most milk in a week (Cow 123 with, 55, litres of milk has produced the most milk in a week)
# Minimum amount is the cow that has produced the least amount of milk in a week(Cow 234 with, 26, litres of milk has produced the least amount of milk in a week)
# Average amount is the average amount of milk produced by all cows in a week (The average amount of milk between each cow is, 34)
# Total is the total amount of milk produced by every cow in a week. (The total amount of milk produced by every cow is, 150)








