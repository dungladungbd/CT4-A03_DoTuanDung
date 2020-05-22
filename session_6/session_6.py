
n = 5


def print_solution(board):
    for i in range(n):
        for j in range(n):
            if len(str(board[i][j])) == 1:
                print("0" + str(board[i][j]), end=" ")
            else:
                print(board[i][j], end=' ')
        print()


def poss_move(board, row, col):
    poss = []
    for nrow in range(-2, n+2):
        for ncol in range(-2, n+2):
            if (nrow - row) * (ncol - col) == 2 or (nrow - row) * (ncol - col) == -2:
                loc = [nrow, ncol]
                poss.append(loc)
    return poss


def valid(board, row, col):
    if board[row][col] == 0:
        return True
    return False


def find_empty(board):
    for row in range(n):
        for col in range(n):
            if board[row][col] == 0:
                return True
    return False


def run(board, row, col, step):
    if not find_empty(board):
        return True
    else:
        poss = poss_move(board, row, col)
        for i in range(len(poss)):
            row, col = poss[i]
            if row in range(n) and col in range(n):
                if valid(board, row, col):
                    step += 1
                    board[row][col] = step
                    if run(board, row, col, step):
                        return True
                    step -= 1
                    board[row][col] = 0
    return False


def solveKT():
    board = [[0 for i in range(n)] for i in range(n)]
    board[0][0] = 1
    row, col = 0, 0
    step = 1
    if run(board, row, col, step):
        print_solution(board)
    else:
        print("No solution.")

solveKT()
