MIN_SENIORS = 10 
MAX_SENIORS = 36
coach = 0
meal = 0
ticket = 0

def handle_seniors(seniors): 
    global coach, meal, ticket
    if seniors > MAX_SENIORS:
        print("Too much seniors")
        return False
    elif seniors < MIN_SENIORS:
        print("Not enought seniors")
        return False
    else: 
        if seniors <= 16:
            coach = 150
            meal = 14
            ticket = 21
            return True
        elif seniors <= 26 and seniors >= 17:
            coach = 190
            meal = 13.50
            ticket = 20
            return True
        else: 
            coach = 225
            meal = 13
            ticket = 19
            return True

while True:
    print("How many seniors for outing?")
    senior = input()
    try: 
        seniors = int(senior)
    except: 
        print("Please input numbers")
        continue
    
    if handle_seniors(seniors): 
        break 
    else: 
        continue 

totalmeal = seniors * meal
totalticket = seniors * ticket
cost = coach + totalmeal + totalticket 
each = cost / seniors
print('total = ' , cost)
print('Cost per person', each)

