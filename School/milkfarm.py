# Milk Production 20/1/23 
identity = []
milk_amount = []

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
# Milking process
for index in range(cows):
    while True:
        print("How much milk produced by", identity[index])
        milk = input()
        try:
            milk = int(milk)
            milk_amount.append(milk)
            break
        except: 
            print("Please input numbers")
            continue
# Finding cow that has produced the most milk in a week
max_milk = -1
cow = 0 
for index in range(len(milk_amount)):
    if milk_amount
        

print("Cows = ", identity)
print("Milk Yields =", milk_amount)


# Maximum amount is the cow that has produced the most milk in a week (Cow 123 with, 55, litres of milk has produced the most milk in a week)
# Minimum amount is the cow that has produced the least amount of milk in a week(Cow 234 with, 26, litres of milk has produced the least amount of milk in a week)
# Average amount is the average amount of milk produced by all cows in a week (The average amount of milk between each cow is, 34)
# Total is the total amount of milk produced by every cow in a week. (The total amount of milk produced by every cow is, 150)








