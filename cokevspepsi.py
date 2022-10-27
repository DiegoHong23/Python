
names = []
cokes = 0 
while (True): 
    print('name?')
    name = input()     
    if name == "end":  
        break
    while (True):
        print("Coke or Pepsi?")
        drink = input()
        if drink == "Coke":
            names.append(name) 
            break
        elif drink == "Pepsi":
            print('rejected')
            break
        else: 
            print('invalid')

print(len(names))
print(names)
