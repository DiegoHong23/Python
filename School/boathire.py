WORKING_HOURS = 7 
TOTAL_BOATS = 10
SHORT_HIRE = 30
LONG_HIRE = 60
SHORT_HIRE_COST = 12
LONG_HIRE_COST = 20
INITIAL_TIME = 10
FINAL_TIME = 17
money = 0

while True:
    print("What time do you want to hire the boat? Please choose a number between 10 and 17")
    times = input()
    try: 
        time = int(times)
    except:
        print("Invalid - not a number")
    if time >= INITIAL_TIME or time <= FINAL_TIME: 
        print("Accept")
        break
    else: 
        print("Invalid - not an available number")
        break 

while True:
    print("How long do you want to hire the boat? Please choose between 30 or 60 (minutes)")
    len = input() 
    try: 
        length = int(len)
    except: 
        print("Invalid - not a number")
        continue 
    if length != SHORT_HIRE or length != LONG_HIRE:
        print("invalid - should be 30 or 60")
        break 
    else: 
        print("Accept")
        continue

if length == SHORT_HIRE:
    money = money + SHORT_HIRE_COST
elif length == LONG_HIRE:
    money = money + LONG_HIRE_COST
print("money taken = ", money)



