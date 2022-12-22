BURGER = ["cheeseburger", "fish burger" ," veggie burger", "no burger" ]
NUMBER_OF_BURGER = [1,2,3,4]
CALORIE_OF_BURGER = [461,431,420,0]
DRINK = ["soft drink", "orange juice", "milk", "no drink"]
NUMBER_OF_DRINK = [1,2,3,4]
CALORIE_OF_DRINK = [130, 160, 118, 0]
SIDE = ["fries", "baked potato", "chef salad", "no side"]
NUMBER_OF_SIDE = [1,2,3,4]
CALORIE_OF_SIDE = [100,57,70,0]
DESSERT = ["apple pie", "sundae", "fruit cup", "no dessert"]
NUMBER_OF_DESSERT = [1,2,3,4]
CALORIE_OF_DESSERT = [167,266,75,0]
calorie = 0

while True: 
    print("Which burger do you want to order?")
    print(BURGER)
    print(NUMBER_OF_BURGER)
    print("Please input number of the burger")
    burger = input()
    try: 
        burger = int(burger)
    except:
        print("invalid")
        continue
    if burger in  NUMBER_OF_BURGER:
        print("Good choice")
        print(CALORIE_OF_BURGER[NUMBER_OF_BURGER.index(burger)])
        calorie += CALORIE_OF_BURGER[NUMBER_OF_BURGER.index(burger)]
        break
    else: 
        print("Not an option") 
        continue

while True: 
    print("Which drink do you want to order?")
    print(DRINK)
    print(NUMBER_OF_DRINK)
    print("Please input number of the drink")
    drink = input()
    try: 
        drink = int(drink)
    except:
        print("invalid")
        continue
    if drink in  NUMBER_OF_DRINK:
        print("Good choice")
        print(CALORIE_OF_DRINK[NUMBER_OF_DRINK.index(drink)])
        calorie += CALORIE_OF_DRINK[NUMBER_OF_DRINK.index(drink)]
        break
    else: 
        print("Not an option") 
        continue

while True: 
    print("Which side do you want to order?")
    print(SIDE)
    print(NUMBER_OF_SIDE)
    print("Please input number of the side")
    side = input()
    try: 
        side = int(side)
    except:
        print("invalid")
        continue
    if side in  NUMBER_OF_SIDE:
        print("Good choice")
        print(CALORIE_OF_SIDE[NUMBER_OF_SIDE.index(side)])
        calorie += CALORIE_OF_SIDE[NUMBER_OF_SIDE.index(side)]
        break
    else: 
        print("Not an option") 
        continue

while True: 
    print("Which dessert do you want to order?")
    print(DESSERT)
    print(NUMBER_OF_DESSERT)
    print("Please input number of the dessert")
    dessert = input()
    try: 
        dessert = int(dessert)
    except:
        print("invalid")
        continue
    if dessert in  NUMBER_OF_DESSERT:
        print("Good choice")
        print(CALORIE_OF_DESSERT[NUMBER_OF_DESSERT.index(dessert)])
        calorie += CALORIE_OF_DESSERT[NUMBER_OF_DESSERT.index(dessert)]
        break
    else: 
        print("Not an option") 
        continue

print("Total calories =", calorie)
    