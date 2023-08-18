n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y, z):
    q = [(x,y)]
    visited[x][y] = True
    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > z and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True


for rain in range(101):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > rain and not visited[i][j]:
                bfs(i, j, rain)
                cnt += 1
    ans.append(cnt)

print(max(ans))
