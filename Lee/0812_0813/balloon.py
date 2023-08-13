import sys
sys.stdin = open('input1.txt')

Testcase = int(input())

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for test in range(Testcase):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    final = 0
    for i in range(N):
        for j in range(M):
            L = Board[i][j]
            mid = L
            for k in range(4):
                for l in range(1, L+1):
                    nx = i + l * dx[k]
                    ny = j + l * dy[k]
                    if (0<=nx<N) and (0<=ny<M):
                        mid += Board[nx][ny]
            if mid >= final:
                final = mid

    print(f'#{test+1}', final)