# Ex 1: Greatest Common Divisor
'''
a = int(input('Insert the first number: '))
b = int(input('Insert the sencond number: '))

def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b-a
    return a

print('The greatest common divisor of the two number is: ',gcd(a,b))
'''


# Ex 2:
'''
sum_ex2 = 0
list_ex2 = []
size_ex2 = int(input('Insert size of the list: '))
for _ in range(size_ex2):
    list_ex2.append(int(input('Insert a number: ')))
for i in range(len(list_ex2)):
    sum_ex2 += list_ex2[i]
min_ex2 = list_ex2[len(list_ex2)-1]
max_ex2 = list_ex2[len(list_ex2)-1]
for i in range(len(list_ex2)-1):
    if list_ex2[i] < min_ex2:
        min_ex2 = list_ex2[i]
    if list_ex2[i] > max_ex2:
        max_ex2 = list_ex2[i]
x = int(input('Insert the number you want to track: '))
x_count = 0
for i in range(len(list_ex2)):
    if list_ex2[i] == x:
        x_count += 1
print('a, The sum of the list is: ',sum_ex2)
print('b, The smallest number in the list is: ',min_ex2)
print('c, The biggest number in the list is: ',max_ex2)
print('d, The number {} appeared {} times. '.format(x,x_count))
'''
# Ex 3:
'''
list_ex3 = []
size_ex3 = int(input('Insert the size of the list: '))
for _ in range(size_ex3):
    list_ex3.append(int(input('Insert a number: ')))


def sort_ex3(listt):
    if len(listt) <= 1:
        return listt
    else:
        a = 0
        b = len(listt)
        i = -1
        for _ in range(len(listt)-1):
            b += i
            if (listt[a] > listt[b] and a < b) or (listt[a] < listt[b] and a > b):
                listt[a], listt[b] = listt[b], listt[a]
                a, b = b, a
                i *= -1
        smaller = listt[:a]
        pivot = [listt[a]]
        bigger = listt[(a+1):]
        sort_smaller = sort_ex3(smaller)
        sort_bigger = sort_ex3(bigger)
        new_list = sort_smaller + pivot + sort_bigger
        return new_list


print(sort_ex3(list_ex3))
'''

# Ex 4: Not finished
'''
n = int(input('Insert the table size: '))
table_ex4 = []
def create_table(table_ex4):
    for i in range(n):
        table_ex4.append([])
        for _ in range(n):
            table_ex4[i].append(0)
    return table_ex4

def print_table(table_ex4):
    for a in range(n):
        for b in range(n):
            print(table_ex4[a][b], end=' ')
        print()    

create_table(table_ex4)
print_table(table_ex4)
'''

#Ex 5: Not finshed
'''
x = input('Insert a string: ')
board = [[' ' for i in range(len(x))] for i in range(len(x))]
def create_board(x,board):
    for a in range(len(x)):
        for b in range(len(x)):
            if b < len(x):
                board[a][b] = x[b]
        x = x[1:]
    return board
def print_board(bo):
    for a in range(len(bo)):
        for b in range(len(bo)):
            print(bo[a][b], end=' ')
        print() 

def find_x(x,board):
    loc, board[0][0] = board[0][0], '*'
    row = 0
    col = 0
    


def find_x_sp(loc,row,col,x,board):




create_board(x,board)
print_board(board)
'''


