import sys


def check(x, y):
    lst = [0] * 10
    for i in range(9):
        lst[sudoku[x][i]] += 1
    for i in range(1, 10):
        if lst[i] > 1:
            return False
    lst = [0] * 10
    for i in range(9):
        lst[sudoku[i][y]] += 1
    for i in range(1, 10):
        if lst[i] > 1:
            return False
    lst = [0] * 10
    n = x // 3
    m = y // 3
    for i in range(3):
        for j in range(3):
            lst[sudoku[3 * n + i][3 * m + j]] += 1
    for i in range(1, 10):
        if lst[i] > 1:
            return False
    return True


def solve(x, y, n):
    if not check(x, y):
        return

    if n == len(blanks):
        for s in sudoku:
            print(*s)
        exit()

    for i in range(1, 10):
        dx, dy = blanks[n]
        sudoku[dx][dy] = i
        solve(dx, dy, n+1)
        sudoku[dx][dy] = 0


sudoku = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
blanks = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blanks.append((i, j))
x, y = blanks[0]
solve(x, y, 0)