# if height < 200 and height > 145 accept
#  else: reject person
names = []
heights = [] 

for athletes in range(20):
    while (True):
        print("name?")
        name = input()
        print("height?")
        height = int(input())
        if height < 200 and height > 145:
            print('accepted')
            names.append(name)
            heights.append(height)
            break
        else: 
            print('invalid')
print(names,heights)

