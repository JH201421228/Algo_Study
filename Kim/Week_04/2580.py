import sys
input = sys.stdin.readline

def row_check(x, n):            # 행 검증
    for i in range(9):          # 같은 숫자 있으면 False
        if sudoku[x][i] == n:
            return False
    return True

def col_check(y, n):            # 열 검증
    for i in range(9):
        if sudoku[i][y] == n:
            return False
    return True

def squ_check(x, y, n):         # 3X3 검증
    nx = (x // 3) * 3           # 첫번째 사각형(왼쪽 위)속 포함되는 자리면
    ny = (y // 3) * 3           # ex) (1,1) < 왼쪽위 가운데
    for i in range(3):
        for j in range(3):
            if sudoku[nx + i][ny + j] == n: # 9칸 모두 순회하며 검증
                return False
    return True

def sudoku_solution(cnt):                   
    if cnt == len(blank):                                                   # 다 돌았으면 빈칸이 없을꺼니까 
        for k in range(9):                                                  # 9줄 반환
            print(*sudoku[k])                                               # 언패킹 오퍼레이터
        exit()                                                              # 함수 탈출 (이거 없으면 답 안나옴)
    x, y = blank[cnt][0], blank[cnt][1]
    for k in range(1, 10):
        if row_check(x, k) and col_check(y, k) and squ_check(x, y, k):      # 검증 완료 됬을 때 즉 겹치는 숫자가 없을 때
            sudoku[x][y] = k                                                # 0을 다른 숫자로 대체
            sudoku_solution(cnt+1)      # 백트래킹
            sudoku[x][y] = 0                                                # 다음 경우에서 겹치는 케이스 있을 경우 앞으로 돌아가서 0으로 바꿔야 함

sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []      # 0인 자리 즉 빵꾸난 자리 찾기
for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:        # 0 == False
            blank.append([i, j])
sudoku_solution(0)