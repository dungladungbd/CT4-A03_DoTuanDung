'''
import math

# Ex1


def get_delta(a, b, c):
    delta = b*b - 4*a*c
    return delta


def quadro(a, b, c):
    delta = get_delta(a, b, c)
    if delta < 0:
        return "No real solution."
    elif delta == 0:
        root = (-b)/(2*a)
        return root
    elif delta > 0:
        root_1 = (-b + math.sqrt(delta))/(2*a)
        root_2 = (-b - math.sqrt(delta))/(2*a)
        return root_1, root_2


# Ex2:
point_1 = []
point_2 = []
point_1.append(int(input("Insert x coordinate of point A: ")))
point_1.append(int(input("Insert y coordinate of point A: ")))
point_2.append(int(input("Insert x coordinate of point B: ")))
point_2.append(int(input("Insert y coordinate of point B: ")))


def get_f(point_1=[], point_2=[]):
    if point_1[0] == point_2[0]:
        if point_2[1] == point_1[1]:
            return "2 points must be different."
        else:
            return "Infinite value of a and b."
    else:
        a = (point_2[1]-point_1[1])/(point_2[0]-point_1[0])
        b = point_1[1] - a*point_1[0]
        return a, b
# pow(a,b) = a mu b
# Ex3:


x = int(input("Nhap he so cua x: "))
y = int(input("Nhap he so cua y: "))
z = int(input("Nhap hang so: "))


def get_dist(point_1, a, b, c):
    distance = abs(a*point_1[0]+b*point_1[1]+c)/(math.sqrt(a*a+b*b))
    return distance


print(get_dist(point_2, x, y, z))
'''

#################### RECURSIVE (đệ quy)
'''
def hanoi_tower_recursion(n):
    """ algorithm to resolve hanoi_tower problem 
    - n: number of disks
    - move: minimal number of moves to solve the problem"""
    if n == 1:
        return 1
    else:
        move = 2*hanoi_tower_recursion(n-1) +1
    return move
print(hanoi_tower_recursion(10))
'''

def find_minimum(list_n = []):
    if len(list_n) == 0:
        return "Cannot find the minimum of an empty list"
    elif len(list_n) == 1:
        minimum_value = list_n[0]
    else:
        if list_n[0] >= list_n[1]:
            del(list_n[0])
        else:
            del(list_n[1])
        minimum_value = find_minimum(list_n)
    return minimum_value

    
#Chua bai:
def find_minimum_2(l):
    if len(l) == 0:
        return "Cannot find the minimum of an empty list"
    elif len(l) == 1:
        return l[0]
    else:
        min_number = find_minimum_2(l[1:])
        min_result = l[0]
        if min_number < min_result :
            min_result = min_number
        return min_result
a = [7,3,4,6]
b = []
print(find_minimum_2(a))
print(find_minimum(a))