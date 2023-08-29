import sys
sys.stdin = open('2580.txt')

# 어떤 자리에 어떤 수를 넣는 것이 가능한지 확인하는 함수
def is_put(i, j, n):
    # 행과 열 먼저 확인
    for k in range(9):
        if Board[i][k] == n or Board[k][j] == n:
            return False

    # 박스 확인
    ni = (i//3)*3
    nj = (j//3)*3
    for m in range(ni, ni+3):
        for l in range(nj, nj+3):
            if Board[m][l] == n:
                return False

    return True

# 스도쿠가 올바른지 확인하는 함수
def is_right():
    # 만약 빈 곳이 없다면 True를 반환
    if not empty:
        return True

    ni, nj = empty.pop()
    for n in range(1, 10):
        if is_put(ni, nj, n):
            Board[ni][nj] = n
            if is_right():
                return True
            Board[ni][nj] = 0
    empty.append((ni, nj))
    return False




Board = [list(map(int, input().split())) for _ in range(9)]
# 빈 곳이 없다면 스도쿠가 완성되었다고 판단할 것임
empty = []
for i in range(9):
    for j in range(9):
        if Board[i][j] == 0:
            empty.append((i, j))

if is_right():
    for i in Board:
        print(*i)