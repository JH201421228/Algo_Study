import sys
sys.stdin = open('balloonboom.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    maximum = 0
    for i in range(N):
        for j in range(M):
            R = Board[i][j]
            mid = Board[i][j]
            for k in range(4):
                for l in range(1, R+1):
                    nx = i + l * dx[k]
                    ny = j + l * dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        mid += Board[nx][ny]
            if mid >= maximum:
                maximum = mid

    print(f'#{test+1}', maximum)