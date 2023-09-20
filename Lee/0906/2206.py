from collections import deque
import sys

sys.stdin = open('2206.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def BFS(start):
    visited = [[-1] * M for _ in range(N)]
    visited[start[0]][start[1]] = 1
    Q = deque([start])
    while Q:
        ni, nj = Q.popleft()
        for k in range(4):
            nx = ni + dx[k]
            ny = nj + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and Board[nx][ny]==0:
                Q.append((nx, ny))
                visited[nx][ny] = visited[ni][nj] + 1
    return visited[N-1][M-1]

N, M = map(int, input().split())
Board = [list(map(int, input())) for _ in range(N)]
can_one=[(0, 0)]
for i in range(N):
    for j in range(M):
        if Board[i][j] == 1:
            can_one.append((i, j))
final = []
for i in can_one:
    Board[i[0]][i[1]] = 0
    a = BFS((0, 0))
    if a!= -1:
        final.append(a)
    Board[i[0]][i[1]] = 1
try:
    print(min(final))
except ValueError:
    print(-1)