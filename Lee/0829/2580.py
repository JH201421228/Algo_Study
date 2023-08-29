import sys

sys.stdin = open('2580.txt')

'''
우리가 스도쿠 풀듯이 풀되 컴퓨터가 할 수 있는 방법을 생각해보자.
1. 가로 세로 박스에서의 중복된 수를 피하며 0을 채워나가는 것
2. 만약 박스를 채워야할 때, 될 수 있는 숫자가 여러개인 경우는
    다른 채울 수 있는 박스들을 채우고 난 후 다시 진행하면 해결될 수 있다.
3. 그래서 한 번 돌아서 해결하는 것이 아닌, 재귀로 해결한다.    
'''


# 해당 좌표에서 그 수가 들어갈 수 있는지 체크 한다.
def is_valid(row, col, num):
    # 행과 열을 한 번에 판단한다.
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # 박스를 확인할 때, 로직 확인
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

# 이 스도쿠가 풀리는지 안풀리는지 확인하는 함수
def solve_sudoku():
    # 0이 있는 곳이 없어지면 스도쿠가 완성되었음을 확인
    if not empty_cells:
        return True

    # 0이 있는 좌표를 가져와서
    row, col = empty_cells.pop()
    # 1부터 9까지 돌며 들어갈 수 있는지 판단한다.
    for num in range(1, 10):
        if is_valid(row, col, num):
            # 만약 4와 9가 들어갈 수 있다면 4가 먼저 들어가게 된다.
            board[row][col] = num
            # 4를 채웠더니 완성했니? -> 재귀로 표현
            if solve_sudoku():
                return True
            # 아니면 4가 아니었던 것이니 다시 0으로 바꿔
            board[row][col] = 0
            # 이러고 다시 for 문을 돌아 9가 들어가게 된다.
    # 모든 경우의 수를 다 해도 안되면 다시 빈 곳으로 처리하고
    empty_cells.append((row, col))
    # 못 푼다고 선언
    return False


# 판 입력받기
board = [list(map(int, input().split())) for _ in range(9)]

# 빈 곳을 찾아서 모아두자
empty_cells = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            empty_cells.append((i, j))

# 풀 수 있으면 출력하고
if solve_sudoku():
    for row in board:
        print(*row)
# 못 풀면 못한다고 말해
else:
    print("제대로 줘")