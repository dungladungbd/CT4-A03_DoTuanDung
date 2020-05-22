'''
1. cho 1 số tự nhiên, tính tổng các chữ số của số này (ví dụ: 1234 có tổng các chữ số là 10)

2. cho 1 số n, tính tổng n số tự nhiên đầu tiên (ví dụ n = 4 -> result = 1 + 2 + 3 + 4 = 10)
 (yêu cầu dùng đệ quy để giải)

3. cho 1 số n, viết chương trình đổi số này thành dạng nhị phân (ví dụ: 7 = 111, 10 = 1010)

4. bài toán tìm đường ra khỏi mê cung. Cho mê cung như sau, trong đó các ô số 0 là không được 
đi vào, còn các ô số 1 là được đi vào:
maze = [ [1, 0, 0, 0], 
         [1, 1, 0, 1], 
         [0, 1, 0, 0], 
         [1, 1, 1, 1] ]
    Bạn khởi đầu ở ô đầu tiên góc trên trái và cần tìm cửa ra ở ô góc dưới cùng bên phải.
    In ra màn hình solution hiển thị đường đi ra khỏi mê cung

5. cho trục tọa độ Oxy, cho tọa độ điểm khởi đầu (sx, sy) và tọa độ điểm đích (dx, dy). 
Viết chương trình kiểm tra xem có thể đi từ điểm khởi đầu tới điểm kết thúc được không 
(return True hoặc False), biết rằng tại mỗi điểm (x,y) bất kì, chỉ có thể di chuyển theo
1 trong 2 cách (x, x + y) hoặc (x + y, y)

6. Cho 2 số tự nhiên x và n, tìm số cách mà x có thể biểu diễn bằng tổng các số tự nhiên 
khác nhau mũ n.
    ví dụ: x = 10, n = 2 -> result = 1 (10 = 1^2 + 3^2)
x = 100, n = 2 -> result = 3 (100 = 10^2 hoặc 100 = 6^2 + 8^2 hoặc 100 = 1^2 + 3^2 + 4^2 + 5^2 + 7^2)

7. cho trục số tự nhiên từ -infinity tới +infinity và số tự nhiên n. Bạn bắt đầu từ điểm 0, 
bạn cần tối thiểu bao nhiêu bước để chạm tới điểm n? Biết rằng bạn có thể di chuyển sang trái hoặc 
phải tùy ý, với điều kiện mỗi lần di chuyển, bạn lại tăng Step lên 1. 
    ví dụ: để đi từ 0 tới 3 bạn cần tối thiểu 2 bước (cụ thể: (0 -> 1) và (1 -> 3))
           để đi từ 0 tới 4 bạn cần tối thiểu 3 bước (cụ thể: (0 -> -1), (-1 -> 1) (1 -> 4))'''
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

# Su dung ham bin()


def de_to_bi(numb):
    if numb == 0:
        return 0
    else:
        return (numb % 2 + 10 * de_to_bi(numb // 2))


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

# Ex 5:


def check(sx, sy, dx, dy):
    if sx * dx > dx * dx or sy * dy > dy * dy:
        return False
    return True


def den_dich(sx, sy, dx, dy):
    if not check(sx, sy, dx, dy):
        return False
    if sx == dx and sy == dy:
        return True
    for i in range(2):
        if i == 0:
            sy += sx
            if den_dich(sx, sy, dx, dy):
                return True
            sy -= sx
        if i == 1:
            sx += sy
            if den_dich(sx, sy, dx, dy):
                return True
            sx -= sy
    return False


def isReachable(sx, sy, dx, dy):
    if abs(sx) > abs(dx) or abs(sy) > abs(dy):
        return False
    if (sx == dx and sy == dy):
        return True

    return (isReachable(sx + sy, sy, dx, dy) or isReachable(sx, sy+sx, dx, dy))


#print(den_dich(10, 7, 79, 55))

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
# Ex 7:


def reachTarget(target):
    target = abs(target)

    sum = 0
    step = 0
    while (sum < target and (sum - target) % 2 != 0):
        step += 1
        sum += step
    return step


def reach(current, step, dest):
    if abs(current) > abs(dest):
        return 2 * abs(dest) - 1

    if current == dest:
        return step

    pos = reach(current + step + 1, step + 1, dest)

    neg = reach(current - step - 1, step + 1, dest)

    return min(pos, neg)


print(reach(0, 0, 12))
