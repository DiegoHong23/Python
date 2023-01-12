# Milk Production 11/1/23 
identity = []
milkamount = []
TOTALMILKPERCOW = 14

while True: 
    print("How many cows?")
    cows = input()
    


while True: 
    print("Please input 3 digit identity code")
    code = input()
    try: 
        code = int(code)
    except: 
        ("Please input numbers")
        continue
    if len(code) == 3: 
        print("valid data")
        break
    else: 
        print('number of digits incorrect')


