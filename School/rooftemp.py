# if temp <= 10 or temp >= 50  for invalid
# if temp >= 10 or temp <= 50  for valid
middaytemp = []
midnighttemp = []

while (True):
    print('middaytemp?')
    temp = int(input())
    if temp >= 10 and temp <= 50: 
        middaytemp.append(temp)
        break
    else:
        print('invalid')
print(middaytemp)

while (True):
    print('midnighttemp?')
    temp = int(input())
    if temp >= 10 and temp <= 50: 
        midnighttemp.append(temp)
        break
    else:
        print('invalid')
print(midnighttemp)
    
    
    


    

