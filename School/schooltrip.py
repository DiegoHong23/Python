max_students = 45
coach = 550
entry = 30

while (True):
    print("students?")
    stud = input()
    try:
        students = int(stud)
    except: 
        print("invalid")
        continue
    if students < 0 and students > 45:
        print("invalid")
    else: 
        break

free = students // 15
fee = (students - free) * entry
total_fee = fee + coach

print(total_fee,'$')



