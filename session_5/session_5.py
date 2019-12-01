board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


print_board(board)


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo, i, [row, col]):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0

    return False


def find_empty(bo):
    for row in range(0, 9):
        for col in range(0, 9):
            if bo[row][col] == 0:
                return row, col
    return None


# pos = [row,col] , thoa man: True, ko thoa man : False
def valid(bo, num, pos):
    for i in range(0, 9):
        if bo[i][pos[1]] == num or bo[pos[0]][i] == num:
            return False
        for j in range(0, 9):
            if pos[0] in range(0, 3) and pos[1] in range(0, 3) and i in range(0, 3) and j in range(0, 3) and bo[i][j] == num:
                return False
            elif pos[0] in range(0, 3) and pos[1] in range(3, 6) and i in range(0, 3) and j in range(3, 6) and bo[i][j] == num:
                return False
            elif pos[0] in range(0, 3) and pos[1] in range(6, 9) and i in range(0, 3) and j in range(6, 9) and bo[i][j] == num:
                return False
            elif pos[0] in range(3, 6) and pos[1] in range(0, 3) and i in range(3, 6) and j in range(0, 3) and bo[i][j] == num:
                return False
            elif pos[0] in range(6, 9) and pos[1] in range(0, 3) and i in range(6, 9) and j in range(0, 3) and bo[i][j] == num:
                return False
            elif pos[0] in range(3, 6) and pos[1] in range(3, 6) and i in range(3, 6) and j in range(3, 6) and bo[i][j] == num:
                return False
            elif pos[0] in range(3, 6) and pos[1] in range(6, 9) and i in range(3, 6) and j in range(6, 9) and bo[i][j] == num:
                return False
            elif pos[0] in range(6, 9) and pos[1] in range(3, 6) and i in range(6, 9) and j in range(3, 6) and bo[i][j] == num:
                return False
            elif pos[0] in range(6, 9) and pos[1] in range(6, 9) and i in range(6, 9) and j in range(6, 9) and bo[i][j] == num:
                return False
    return True
solve(board)
print()
print_board(board)
