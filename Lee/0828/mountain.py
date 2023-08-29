import sys
sys.stdin = open('mountain.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS(S):
    global K
    Q = [S]
    move = 0
    while Q:
        now = Q.pop(0)
        move += 1
        for k in range(4):
            ni = now[0] + dx[k]
            nj = now[1] + dy[k]
            if 0 <= ni < N  and 0 <= nj < N and Board[ni][nj] - K < Board[now[0]][now[1]]:
                Q.append((ni, nj))
                if Board[ni][nj] >= Board[now[0]][now[1]]:
                    K = 0
                if Board[ni][nj] == mini - K or Board[ni][nj] == mini:
                    return move
    return

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    maxi = 0
    max_point = []
    mini = 21
    min_point = []
    for i in range(N):
        for j in range(N):
            if Board[i][j] >= maxi:
                maxi = Board[i][j]
            if Board[i][j] <= mini:
                mini = Board[i][j]
    for i in range(N):
        for j in range(N):
            if Board[i][j] == maxi:
                max_point.append((i, j))
            if Board[i][j] == mini:
                min_point.append((i, j))

    final = []
    for i in max_point:
        final.append(BFS(i))
    print(final)