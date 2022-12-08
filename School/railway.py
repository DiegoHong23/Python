#EMR 30/11/22
times = [9,11,13]
seats = [80,80,80]
COST = 25
total = 0

total_seats = 8 * (80 * 6) 
total_passengers = 0
print("total seats", total_seats)
while True:
    print("train times \t  =", times)
    print("available seats\t =", seats)

    print("What time do you want to choose?")
    t = input()
    try:
        time=int(t)
    except:
        print("Invalid- Not a number")
    if time == 9:
        print("9am Train Selected")
        if seats[0]==0:
            print("non available")
        else: 
            seats[0]=-10
            print("Ticket for train purchased")
    if time == 11:
        print("11am Train Selected")
        if seats[1]==0:
            print("non available")
        else:
            seats[1]=-10
            print("Ticket for train purchased")
    if time == 13:
        print("13pm Train Selected")
        if seats[2]==0:
            print("non available")
        else: 
            seats[2]=-10
            print("Ticket for train purchased")
    else:
        print("invalid option")
        break

total+=COST

print("the total cost of your ticket is", total)
