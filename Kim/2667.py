dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = [(x, y)]
    visited[x][y] = True
    cnt = 1
    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and arr[x][y] == 1:
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    cnt += 1
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return cnt


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
ans = []

for i in range(n):
    for j in range(n):
        if arr[i][j] and visited[i][j] == 0:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
for i in ans:
    print(i)