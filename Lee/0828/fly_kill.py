import sys
sys.stdin = open('fly_kill.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    final_1 = 0
    final_2 = 0
    for i in range(N):
        for j in range(N):
            mid_1 = Board[i][j]
            mid_2 = Board[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni_1 = i + l * dx[k]
                    nj_1 = j + l * dy[k]
                    ni_2 = i + l * di[k]
                    nj_2 = j + l * dj[k]
                    if 0 <= ni_1 < N and 0 <= nj_1 < N:
                        mid_1 += Board[ni_1][nj_1]
                    if 0 <= ni_2 < N and 0 <= nj_2 < N:
                        mid_2 += Board[ni_2][nj_2]
            if mid_1 >= final_1:
                final_1 = mid_1
            if mid_2 >= final_2:
                final_2 = mid_2
    print(f'#{tc}',max(final_1, final_2))
