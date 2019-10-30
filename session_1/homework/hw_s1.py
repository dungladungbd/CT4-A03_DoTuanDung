# Find the factorial of an integer
loop = True
f = 1
while loop:
    n = input("Input a number: ")
    if not n.isdigit():
        print("Please input an integer !!! ")
        continue
    n = int(n)
    if n <0 :
        print("Invalid number !!!")
        continue
    loop = False
    for i in range(1,n+1):
        f = f*i
print("The factorial of {} is: ".format(n),f)


print()


#Count the number of digits a number:
numb = input("Input a number: ")
while loop :
    if not numb.isdigit():
        print("Please input an integer !!! ")
        continue
    loop = False
print("The length of {} is: ".format(numb), numb.__len__())


