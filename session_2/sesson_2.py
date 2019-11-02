'''
TODO:
NOTE: 
loop = True
number = 10
while loop:
    x = input("Input a number: ")
    try:
        n = int(x)
        a = 10/n
        print(a)
        loop = False
    except ValueError:  # expect Exception:   (danh cho tat ca cac loi xay ra, nhung ko nen vi co nhung bug quan trong can dung lai)
        print("Invalid number!")
    except ZeroDivisionError:
        print("Your number must not be 0")
'''
'''
NOTE: loop items and index
for index, item in enumerate(menu):
    print(index, item)
NOTE: update
menu[1], menu[2] = menu[2], num[1]     dao vi tri 2 gia tri
'''
'''
from random import randint
input_list = []
for i in range(10):
    input_list.append(randint(1, 10))
print(input_list)
# a
list_a = []
for i in range(3):
    list_a.append(input_list[i])
print(list_a)
print(input_list[:3])
# b
list_b = []
for i in range(2, -1, -1):
    list_b.append(input_list[9-i])
print(list_b)
print(input_list[-3:])
# c
for i in range(9):
    for n in range(i+1, 10):
        if input_list[i] > input_list[n] and i < n:
            input_list[i], input_list[n] = input_list[n], input_list[i]
print(input_list)
input_list.sort()
# d
list_d = []
for i in range(9, -1, -1):
    list_d.append(input_list[i])
print(list_d)
input_list.sort(reverse=True)
print(input_list)
'''
'''
List Slicing
nums = [1,2,3,4,5,1,6,3,11,7,5]
nums[:] == nums
nums[3:] == [4,5,1,6,3,11,7,5]
nums[:-3] == [4,5,1,6,3]
lay dau bo duoi
'''

'''
from random import randint
input_list = []
for i in range(10):
    input_list.append(randint(1, 10))
print(input_list)

# Selection Sort
for i in range(len(input_list)-1):
    min_index = i
    for n in range(i+1, len(input_list)):
        if input_list[min_index] > input_list[n]:
            min_index = n
    input_list[min_index], input_list[i] = input_list[i], input_list[min_index]
print(input_list)

# Bubble Sort
swapped = True
while swapped:
    swapped = False
    for i in range(len(input_list)-1):
        if input_list[i] < input_list[i+1]:
            input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
            swapped = True
print(input_list)
'''

'''
NOTE: change a key to another key
person["sex"] = person.pop("gender")
'''


list1= [1, 3, 4, 16, 32, 8, 64, 4, 128, 2, 256, 32]
list2 = [16, 2, 4, 2, 128, 64, 16, 7, 1, 64, 32, 16, 5, 8]
print("Cac cap so co tich bang 256 la: ")
import math
def tim_uoc_so(n,lst):
    n = math.floor(n)
    x = math.floor(math.sqrt(n))
    for i in range(1,x+1):
        if n % i == 0 :
            lst.append


avai_ans = {
    'a0' : [1,256],
    'a1' : [2,128],
    'a2' : [4,64],
    'a3' : [8,32],
    'a4' : [16,16],
}

for key, value in avai_ans.items():
    index1 = -1
    index2 = -1
    for i in range(list2.__len__()):
        if list2[i] == value[0] and index1 == -1 :
            index1 = i
        elif list2[i] == value[1] and index2 == -1:
            index2 = i
    if index1 != -1 and index2 != -1:
        print("{} va {} o vi tri so {} va {}".format(value[0],value[1],index1+1,index2+1))

    


