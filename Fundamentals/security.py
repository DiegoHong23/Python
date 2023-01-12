#Validation Types 

while True:
    print('name?')
    name = input()
    if name == '':
        print('invalid - presence check')
        continue
    else:
        print('valid - presence check')
        break

while True:
    print('Telephone number?')
    telephone = input()
    if len(telephone) <= 15: 
        print('valid data')
        break



while True:
    print('xp level?')
    xp = input()
    if xp <= 5 or xp >= 1: 
        print('valid data')
        break
    else:
        print('invalid')
        continue



