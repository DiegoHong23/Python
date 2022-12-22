CALORIE_OF_BURGER = [461,431,420,0]
CALORIE_OF_DRINK = [130, 160, 118, 0]
CALORIE_OF_SIDE = [100,57,70,0]
CALORIE_OF_DESSERT = [167,266,75,0]

calorie = 0

burger = int(input())
calorie += CALORIE_OF_BURGER[burger-1]
 
side = int(input())
calorie += CALORIE_OF_SIDE[side-1]
 
drink = int(input())
calorie += CALORIE_OF_DRINK[drink-1]

dessert = int(input())
calorie += CALORIE_OF_DESSERT[dessert-1]

print(f"Your total Calorie count is {calorie}.")
    