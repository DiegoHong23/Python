MIN_SENIORS = 10 
MAX_SENIORS = 36
while True:
    print("How many seniors for outing?")
    senior = input()
    try: 
        seniors = int(senior)
    except: 
        print("Please input numbers")
        continue
    if seniors > MAX_SENIORS:
        print("Too much seniors")
        continue
    elif seniors < MIN_SENIORS:
        print("Not enought seniors")
        continue
    else: 
        if seniors <= 16:
            coach = 150
            meal = 14
            ticket = 21
            break
        elif seniors <= 26 and seniors >= 17:
            coach = 190
            meal = 13.50
            ticket = 20
            break
        else: 
            coach = 225
            meal = 13
            ticket = 19
            break

totalmeal = seniors * meal
totalticket = seniors * ticket
cost = coach + totalmeal + totalticket 
each = cost / seniors
print('total = ' , cost)
print('Cost per person', each)








    



