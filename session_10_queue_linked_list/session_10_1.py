''' Đề bài : Bàn cờ nxn đặt n con hậu sao cho ko con nào ăn đc nhau
'''


n = int(input('Input a number:'))

table = []

count = 0


for i in range(n):
    table.append([])
    for j in range(n):
        table[i].append(0)

def print_table(table):
    for i in range(len(table)):
        for j in range(len(table)):
            print(table[i][j], end = '  ')
        print()

def unavail_square(table, row, col ):
    for i in range(len(table)):
        if i == row:
            for j in range(len(table)):
                if j != col and table[i][j] != 1:
                    table[i][j] += 2
        if i == col:
            for j in range(len(table)):
                if j != row and table[i][j] != 1:
                    table[j][i] += 2
    d_row = [1,1,-1,-1]
    d_col = [1,-1,1,-1]
    for i in range(4):
        n_row = row
        n_col = col
        while True:
            n_row += d_row[i]
            n_col += d_col[i]
            if n_col <0 or n_col >= len(table) or n_row < 0 or n_row >= len(table):
                break
            else:
                table[n_row][n_col] += 2
        
    # try:
    #     for i in range(1,len(table)):
    #         table[row-i][col+i] += 2
    #         table[row+i][col-i] += 2
    #         table[row+i][col+i] += 2
    #         table[row-i][col-i] += 2
    # except IndexError :
    #     pass

def undo_unvail_square(table,row,col):
    for i in range(len(table)):
        if i == row:
            for j in range(len(table)):
                if j != col and table[i][j] != 1:
                    table[i][j] -= 2
        if i == col:
            for j in range(len(table)):
                if j != row and table[i][j] != 1:
                    table[j][i] -= 2
    d_row = [1,1,-1,-1]
    d_col = [1,-1,1,-1]
    for i in range(4):
        n_col = col
        n_row = row
        while True:
            n_row += d_row[i]
            n_col += d_col[i]
            if n_col <0 or n_col >= len(table) or n_row < 0 or n_row >= len(table):
                break
            else:
                table[n_row][n_col] -= 2
        table[row][col] = 2
    # try:
    #     for i in range(len(table)):
    #         if table[row+i][col+i] != 1:
    #             table[row+i][col+i] -= 2
    #         if table[row-i][col-i] != 1:
    #             table[row-i][col-i] -= 2
    # except IndexError :
    #     pass

def check_empty(table):
    for row in range(len(table)):
        for col in range(len(table)):
            if table[row][col] == 0:
                return row, col
    return None

def clean_table(table):
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] != 1:
                table[i][j] = 0    

def is_done(table):
    queens = 0
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 1:
                queens += 1
    return queens == n


def solve(table):
    if is_done(table) :
        # clean_table(table)
        return True
    else:
        for _ in range(len(table)):
            find = check_empty(table)
            if find == None:
                return False  
            else:
                row, col = find

                table[row][col] = 1
                unavail_square(table,row,col)
                print_table(table)
                print()
                if solve(table):
                    return True
                undo_unvail_square(table,row,col)
                print_table(table)
                print()
                table[row][col] = 2
    return False
            
# table[0][0]= 1
# unavail_square(table,0,0)
solve(table)
print_table(table)




