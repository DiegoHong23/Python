cows = [123, 456]
milks = [34, 25]

cows_milks =  [
    [34, 25, 67, 12, 98],
    [23, 25, 67, 32, 98]
]

max_milk = -1
cow = 0
for index in range(len(milks)):
    if milks[index]>max_milk:
        max_milk=milks[index]
        cow=cows[index]

print(cow, 'has produced', max_milk,'litres of milk')

total_milk = 0
for index in range(len(milks)):
    total_milk+=milks[index]
    
print(total_milk)

for i in range(len(cows_milks)):
    for j in range(len(cows_milks[i])):
        print(cows_milks[i][j])
# print(cows_milks[0][3])
# print(cows_milks[1][3])

cows_milks.append([42,12,34,56,70])
cows_milks[2].append(80)
# cows_milks.insert(cows_milks[2][4],80)
print(cows_milks)   





