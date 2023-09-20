from collections import deque
import sys

sys.stdin = open('2206.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def BFS(i, j, c):
    Q = deque([(i, j, c)])
    visited[i][j][c] = 1
    while Q:
        i, j, c = Q.popleft()

        if i == N - 1 and j == M - 1:
            return visited[i][j][c]

        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue

            if Board[ni][nj] == 1 and c == 0:
                visited[ni][nj][1] = visited[i][j][0] + 1
                Q.append((ni, nj, 1))

            elif Board[ni][nj] == 0 and visited[ni][nj][c] == -1:
                visited[ni][nj][c] = visited[i][j][c] + 1
                Q.append((ni, nj, c))

    return -1


N, M = map(int, input().split())
Board = [list(map(int, input())) for _ in range(N)]
visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
print(BFS(0, 0, 0))
