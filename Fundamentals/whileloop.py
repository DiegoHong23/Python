# i = 1 
# while (i < 3): 
#     print(i)
#     i+=1 

# while (True):
#     print(i)
#     i+=1 
#     if(i >= 3):
#         break

# names = []
# print('Type in names, input "end" when finished') 
# name = input()
# while (name != "end"):
#     names.append(name)
#     name = input()
    
# print(names)

names = []
print('Type in names, input "end" when finished')
while (True): 
    name = input()     # 1
    if name == "end":  # 3
        break
    names.append(name) # 2
print(names)

    




