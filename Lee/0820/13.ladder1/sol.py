import sys
sys.stdin = open('input (9).txt')

# 델타탐색(우, 좌, 상)
di = [0, 0, -1]
dj = [1, -1, 0]

for _ in range(10):
    test = int(input())
    Board = [list(map(int, input().split())) for _ in range(100)]

    # 출발점 찾자
    start_i = 99
    start_j = 0
    for j in range(100):
        if Board[99][j] == 2:
            start_j = j

    # 위로 올라갈 것 => 델타 탐색을 통해 1을 찾을 것(왔던 길을 다시 가지 않기 위해 지나온 길은 0으로 수정)
    while start_i != 0:
        Board[start_i][start_j] = 0
        for k in range(3):
            ni = start_i + di[k]
            nj = start_j + dj[k]
            if 0 <= nj < 100 and Board[ni][nj] == 1:
                start_i = ni
                start_j = nj
                break
    print(f'#{test}', start_j)
