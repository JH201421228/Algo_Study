import sys
sys.stdin = open('2206.txt')

from collections import deque

def bfs(start_x, start_y, start_z):
    queue = deque()
    queue.append((start_x, start_y, start_z))

    while queue:
        x, y, z = queue.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y][z]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if arr[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1   # 이동할때 +1씩 카운트 해주기
                queue.append((nx, ny, 1))   # 큐에 다가 벽을 부셨다고 표시됨

            elif arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
    return -1


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

print(bfs(0, 0, 0))