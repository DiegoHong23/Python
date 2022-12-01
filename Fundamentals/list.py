fruit_list = ["apple", "banana", "cherry"]
print(fruit_list)
print(fruit_list[1])
print(fruit_list[-1])
print(fruit_list[0:2])

print(len(fruit_list))
fruit_list = []
fruit_list.append("orange")

print(fruit_list)

print(len(fruit_list))

other_list = ["apple", "banana", "cherry", 1, 10, "a", 5.3]
if "apple" in fruit_list:
    print("Yes, 'apple' is in the fruits list")

# Add fruit to fruit_list from end
fruit_list.append("orange")
print(fruit_list)

# Add fruit to fruit_list from middle by index
fruit_list.insert(1, "Pear")
print(fruit_list)

# Modify item
fruit_list[1] = "blackcurrant"
print(fruit_list)

# Remove specific item
fruit_list.remove("banana")
print(fruit_list)

# Removes the specified index, or the last item if index is not specified
fruit_list.pop()  # Remove the last element
fruit_list.pop(1) # Remove fruit_list[1]
# Em
fruit_list.clear() #Empties the list       
