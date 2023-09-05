import sys


def check(x, y):
    # 가로 검사
    lst = [0] * 10
    for i in range(9):
        lst[sudoku[x][i]] += 1
    for i in range(1, 10):
        if lst[i] > 1:
            return False
        
    # 세로 검사
    lst = [0] * 10
    for i in range(9):
        lst[sudoku[i][y]] += 1
    for i in range(1, 10):
        if lst[i] > 1:
            return False
        
    # 3X3 박스 검사
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
    # 가로, 세로, 3X3 검사 False면 return
    if not check(x, y):
        return

    # 스도쿠 완성되면 print
    if n == len(blanks):
        for s in sudoku:
            print(*s)
        exit()

    # 빈칸에 1~9 숫자 넣으면서 백트래킹
    for i in range(1, 10):
        dx, dy = blanks[n]
        sudoku[dx][dy] = i
        solve(dx, dy, n+1)
        sudoku[dx][dy] = 0


sudoku = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
blanks = []
# 스도쿠 빈칸 좌표 찾아 blanks에 넣기
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blanks.append((i, j))
x, y = blanks[0]
solve(x, y, 0)