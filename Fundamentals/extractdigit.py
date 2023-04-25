# number = input()
# # for i in range(len(number)):
# #     print(number[i])
# # print(number[1])
# # print(number[2])
# # print(number[3])
# # print(number[4])
# for i in range(len(number)):
#     print(number[i])

# number = int(input())
# number = number % 10
# print(number)
# for i in range(len(number)):
    # print(number[i])

# def get_digit(num):
#     if num < 10:
#         print(num)
#     else:
#         get_digit(num // 10)
#         print(num % 10)
# number = int(input())
# while(number >= 10):
#     digit = number % 10
#     number = number / 10
#     print(digit)

# n = int(input())
# # while n:
# #     n, remainder = divmod(n, 10)
# #     print(remainder)
# n = n % 10
# print(n)
# n = int(input()) 
# # while n:
#     n = n % 10
#     print(n)
n = int(input())
while n > 0: 
    d = n % 10 
    # n = n // 10
    d = int(d)
    n = n / 10
    print(d)
print(n)







