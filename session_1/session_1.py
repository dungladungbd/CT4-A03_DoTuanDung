# import random
# a = 1
# b = 100

# while True:
#     i = random.randint(a,b)
#     print("So cua ban co phai la: ",i)
#     x = input('So sanh voi so cua ban: ')
#     if x == 'c':
#         print("So cua ban nghi la: ",i)
#         break
#     if x == 'l':
#         a = i+1
#     if x == 's':
#         b = i

# comp_num = random.randint(1, 100)
# loop = True
# while loop:
#     player_num = int(input('Your guess is: '))
#     if player_num == comp_num:
#         print("YOU ARE CORRECT!!!!")
#         loop = False
#     if player_num > comp_num:
#         print("Your number is too big.")
#     if player_num < comp_num:
#         print("Your number is too small.")
'''
user = str(input("Type in your number: "))
while loop:
    if user.isdigit() == True:
        loop = False
        print("Your number's length is: ", user.__len__()) # == print("Your number's length is: {}".format(user.__len__()))
    else:
        print("Please input an integer!")
'''
'''
floor_division = 100//7
modulus = 100 % 7
'''
# numb = int(input("Input an integer > 1: "))
# loop = True
# while loop:
#     if numb < 2:
#         print("Invalid number!")
#     else :
#         loop = False
#         print("Those even numbers smaller than {} are: ".format(numb), end=" ")
#         for i in range(2,numb + 1,2):
#             print(i, end=' ')

# numb = int(input("Input an integer > 1: "))
# loop = True
# while loop:
#     if numb < 2:
#         print("Invalid number!")
#     else :
#         loop = False
#         print("Those even numbers smaller than {} are: ".format(numb), end=" ")
#         if numb % 2 == 0:
#             for i in range(numb,1,-2):
#                 print(i, end=' ')
#         else:
#             for i in range(numb-1,1,-2):
#                 print(i, end=' ')

import math

def pttsnt(n):
    s = 0
    x = math.floor(math.sqrt(n))
    for i in range(2,x+1):
        if n % i == 0:
            s += 1
    if s == 0:
        print('Your number is a prime number')
    else:
        print('Your number is not a prime number')

numb = int(input("Input your number: "))
if numb < 2:
    print('Your number is not a prime number')
else:
    pttsnt(numb)
