from collections import deque
import sys

sys.stdin = open('2206.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def BFS(start):
    visited[start[0]][start[1]] = 1
    Q = deque([start])
    while Q:
        ni, nj, c = Q.popleft()
        for k in range(4):
            nx = ni + dx[k]
            ny = nj + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if c == 0:
                    if Board[nx][ny] == 0 and visited[nx][ny] == -1:
                        Q.append((nx, ny, 0))
                        visited[nx][ny] = visited[ni][nj] + 1
                else:
                    if Board[nx][ny] == 0:
                        Q.append((nx, ny, 1))
                        visited[nx][ny] = visited[ni][nj] + 1
                    elif Board[nx][ny] == 1:
                        Q.append((nx, ny, 0))
                        visited[nx][ny] = visited[ni][nj] + 1
            if nx == N - 1 and ny == M - 1:
                return visited[nx][ny]


N, M = map(int, input().split())
Board = [list(map(int, input())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
start = (0, 0, 1)

print(BFS(start))
