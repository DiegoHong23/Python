x = 3
y = 5
z = 7
o = 1
def lcm(x, y, z):
    result = 1
    global o
    while True: 
        result+=1
        if (not result % x < 1) and (not result % y ) and (not result % z):
        # if (v % x == 0) and (v % y == 0):
            break
    o = 10
    return result
# lcm(x, y, z)
# print(lcm(x,y,z))
result = lcm(x,y,z)
print(result)
