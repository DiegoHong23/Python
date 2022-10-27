animal = input('Please input "Hamster", "Gerbil" or "Snake":\n')
weight = int(input('Please input number of animal weight:\n'))
if (animal == "Hamster") or  (animal == "Gerbil"): 
    if (weight >= 60) and (weight <= 90):
        print("accepted")
    else:
        print(animal, "weight is outside of the health range.")
elif (animal == "Snake"):
    if (weight >= 800) and (weight <= 900):
        print("accepted")
    else:
        print(animal, "weight is outside of the health range.")



