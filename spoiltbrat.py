bad_friends =[]
good_friends = []
print("")
name = input()      # End
height = int(input()) 
width = int(input())
depth = int(input())
weight = int(input())
paper = input()     # Expensive or Cheap
while (name != "End"):
    if (height > 50) and (width > 50) and (depth > 50) and (weight > 10) and (paper == "expensive looking"):
        good_friends.append(name) 
    else: 
        bad_friends.append(name)
    
    print("")
    name = input()      # End
    height = int(input()) 
    width = int(input())
    depth = int(input())
    weight = int(input())
    paper = input()     # Expensive or Cheap

print(good_friends,"Thanks")
print(bad_friends,"complain")