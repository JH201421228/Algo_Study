from collections import deque

def bfs(x, y, v):
    global ans
    q = deque()
    q.append((x, y))
    ans += 1
    v[y][x] = 2
    while q:
        x, y = q.popleft()
        for k in range(4):
            ny = y + direct[k][0]
            nx = x + direct[k][1]
            if 0 <= ny < N and 0 <= nx < M and v[ny][nx] == 1:
                v[ny][nx] = 2
                q.append((nx, ny))


direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for t in range(int(input())):
    M, N, K = map(int, input().split())
    MAP = [[0] * M for _ in range(N)]
    for _ in range(K):
        b, a = map(int, input().split())
        MAP[a][b] = 1

    ans = 0
    for i in range(M):
        for j in range(N):
            if MAP[j][i] == 1:
                bfs(i, j, MAP)

    print(ans)