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
            milk_amount.append([])
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
            milk_amount[index].append(milk)
            break
        except: 
            print("Please input numbers")
            continue

# 

        

print("Cows = ", identity)
print("Milk Yields =", milk_amount)