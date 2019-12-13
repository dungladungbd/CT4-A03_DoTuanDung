
# Ex 1:


def tong_chu_so(numb):
    s = 0
    for _ in range(len(str(numb))):
        s += numb % 10
        numb = numb // 10
    return s

# Ex 2:


def tong_so_tu_nhien(numb):
    if numb == 1:
        return 1
    else:
        numb += tong_so_tu_nhien(numb-1)
    return numb

# Ex 3:


def decimal_to_binary(numb):
    s = ''
    for _ in range(numb):
        s = str(numb % 2) + s
        numb = numb // 2
    return int(s)


# Ex 4:
maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]


def print_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze)):
            if j == len(maze) - 1:
                print(maze[i][j])
            else:
                print(maze[i][j], end=' ')


def poss_move(maze, row, col):
    if row == 0:
        if maze[row][col+1] == 1 or maze[row][col-1] == 1 or maze[row+1][col] == 1:
            return True
    elif col == 0:
        if maze[row][col+1] == 1 or maze[row - 1][col] == 1 or maze[row+1][col] == 1:
            return True
    elif row == len(maze)-1:
        if maze[row][col+1] == 1 or maze[row][col-1] == 1 or maze[row - 1][col] == 1:
            return True
    elif col == len(maze)-1:
        if maze[row][col-1] == 1 or maze[row - 1][col] == 1 or maze[row+1][col] == 1:
            return True
    else:
        if maze[row][col+1] == 1 or maze[row][col-1] == 1 or maze[row - 1][col] == 1 or maze[row+1][col] == 1:
            return True
    return False


def move(maze, row, col):
    if maze[len(maze)-1][len(maze)-1] == 'x':
        print_maze(maze)
    elif not poss_move(maze, row, col):
        return False
    elif poss_move(maze, row, col):
        if row == 0:
            if maze[row][col+1] == 1:
                col += 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                col -= 1
            elif maze[row][col-1] == 1:
                col += 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                col -= 1
            elif maze[row+1][col] == 1:
                row += 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                row -= 1
        elif col == 0:
            if maze[row][col+1] == 1:
                col += 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                col -= 1
            elif maze[row+1][col] == 1:
                row += 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                row -= 1
            elif maze[row-1][col] == 1:
                row -= 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                row += 1
        elif row == len(maze) - 1:
            if maze[row][col+1] == 1:
                col += 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                col -= 1
            elif maze[row][col-1] == 1:
                col += 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                col -= 1
            elif maze[row-1][col] == 1:
                row -= 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                row += 1
        elif col == len(maze) - 1:
            if maze[row][col-1] == 1:
                col += 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                col -= 1
            elif maze[row+1][col] == 1:
                row += 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                row -= 1
            elif maze[row-1][col] == 1:
                row -= 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                row += 1
        else:
            if maze[row][col+1] == 1:
                col += 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                col -= 1
            elif maze[row][col-1] == 1:
                col += 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                col -= 1
            elif maze[row+1][col] == 1:
                row += 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                row -= 1
            elif maze[row-1][col] == 1:
                row -= 1
                maze[row][col] = 'x'
                if move(maze, row, col):
                    return True
                maze[row][col] = 1
                row += 1
    return False


def escape_dungeon(maze):
    maze[0][0] = 'x'
    row = 0
    col = 0
    move(maze, row, col)

#Ex 5:
def check(sx,sy,dx,dy):
    if sx * dx > dx * dx or sy * dy > dy* dy:
        return False
    return True

def den_dich(sx, sy, dx, dy):
    if not check(sx,sy,dx,dy):
        return False
    if sx == dx and sy == dy:
        return True
    for i in range(2):
        if i == 0:
            sy += sx
            if den_dich(sx,sy,dx,dy):
                return True
            sy -= sx
        if i == 1:
            sx += sy
            if den_dich(sx,sy,dx,dy):
                return True
            sx -= sy
    return False        

print(den_dich(10,7,79,55))

'''
# Ex 6:
def tong_so_mu(x, n):
    x = int(x)
    n = int(n)
    s = 0
    ways = 0
    numb_list = []
    maxx = pow(x,1/2) //1 +1 
    for i in range(1 , int(maxx)):
        numb_list.append(i)
    for i in numb_list:
        for j in range(i):
            k = 1
            while k < int(maxx) :
                s += pow(k,n)
                if s == x:
                    ways += 1
                s = 0
                k += 1
    
    print(ways)


tong_so_mu(9,2)
'''

