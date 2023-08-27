import sys

sys.stdin = open('Othello.txt')

# 델타 탐색 방향 (다이얼 처럼 1, 2, 3, 6, 9, 8, 7, 4) 순서
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
# 종료 조건은 빈 거를 만나거나 자기랑 같은 색 만날 때 까지


T = int(input())
for tc in range(1, T+1):
    # N : 보드(4, 6, 8) , M : 시행 횟수
    N, M = map(int, input().split())
    # 보드 제작 및 기본 세팅
    Board = [[0]*N for i in range(N)]
    Board[N//2][N//2] = 2
    Board[N//2-1][N//2-1] = 2
    Board[N//2-1][N//2] = 1
    Board[N//2][N//2-1] = 1
    # a, b좌표, c: 색(1:흑돌, 2: 백돌)
    for _ in range(M):
        j, i, c = map(int, input().split())
        Board[i-1][j-1] = c
        for k in range(8):
            l = 1
            ni = i-1 + l * dx[k]
            nj = j-1 + l * dy[k]
            if 0 <= ni < N and 0 <= nj < N:
                while Board[ni][nj] != c and Board[ni][nj] != 0:
                    l += 1
                    ni += dx[k]
                    nj += dy[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        continue
                    else:
                        break
                if 0 <= ni < N and 0 <= nj < N and Board[ni][nj] == c:
                    for p in range(1, l):
                        ni -= dx[k]
                        nj -= dy[k]
                        Board[ni][nj] = c

    c1 = 0
    c2 = 0
    for i in range(N):
        for j in range(N):
            if Board[i][j] == 1:
                c1 += 1
            elif Board[i][j] == 2:
                c2 += 1
    print(f'#{tc}', c1, c2)