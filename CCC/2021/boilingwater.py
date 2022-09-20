temperature = int(input())
atmospheric = 5 * temperature - 400 
print(atmospheric)
if atmospheric == 100: 
    print(0)
if atmospheric > 100:
    print(-1)
if atmospheric < 100: 
    print(1)
