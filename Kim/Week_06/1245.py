import sys
# input = sys.stdin.readline

direct = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def dfs(x, y):
    global flag
    visited[x][y] = True

    for k in range(8):
        nx = x + direct[k][0]
        ny = y + direct[k][1]
        if 0 <= nx < N and 0 <= ny < M:
            if MAP[x][y] < MAP[nx][ny]:
                flag = False
            if not visited[nx][ny] and MAP[nx][ny] == MAP[x][y]:
                dfs(nx, ny)


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            flag = True
            dfs(i, j)

            if flag:
                cnt += 1

print(cnt)