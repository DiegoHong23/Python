fruit_list = ["orange", "banana","peach", "che", "apple", "banana"]
# # fruit_list = [4, 2, 9, 1]
# # Sort the list, the list will change order
# fruit_list.sort(reverse=True)
# print(fruit_list)
# # Make a new list with sorted
# # new_list = sorted(old_list)
# # print(old_list)
# # print(new_list)
# print(fruit_list[1])
# print(fruit_list[-1])
# print(fruit_list[0:2])



# print(len(fruit_list))
# fruit_list = []
# fruit_list.append("orange")

# print(fruit_list)

# print(len(fruit_list))

# other_list = ["apple", "banana", "cherry", 1, 10, "a", 5.3]
# if "apple" in fruit_list:
#     print("Yes, 'apple' is in the fruits list")

# # Add fruit to fruit_list from end
# fruit_list.append("orange")
# print(fruit_list)

# # Add fruit to fruit_list from middle by index
# fruit_list.insert(1, "Pear")
# print(fruit_list)

# # Modify item
# fruit_list[1] = "blackcurrant"
# print(fruit_list)

# # Remove specific item
# fruit_list.remove("banana")
# print(fruit_list)

# # Removes the specified index, or the last item if index is not specified
# fruit_list.pop()  # Remove the last element
# fruit_list.pop(1) # Remove fruit_list[1]
# Em
# fruit_list.clear() #Empties the list       
# Iterate list by index
print(len(fruit_list))
for index in range(len(fruit_list)): #For example:5 
    print(index)
    print(fruit_list[index])    # i: 0,1,2,3,4

# Iterate list by item 
for fruit in fruit_list: # Variable: fruit 
    print(fruit)         # The value is in the variable fruit