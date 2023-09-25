# 벽(#)
# 지나갈 수 있는 공간(.)
# 지훈이의 초기 위치(J)
# 불이난 공간
import sys
from collections import deque
sys.stdin = open('a.txt')
input = sys.stdin.readline

# 델타 탐색 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
Board = [list(input())[:M] for _ in range(N)]
visited = [[0]*M for _ in range(N)]
# print(Board)
# print(visited)
fire_idx = deque()
exit_idx = []
start = 0
for i in range(N):
    for j in range(M):
        if Board[i][j] == '#':
            visited[i][j] = 1
        elif Board[i][j] == 'J':
            start = (i, j, 0)
            visited[i][j] = 1
        elif Board[i][j] == 'F':
            fire_idx.append((i, j))
            visited[i][j] = 1
        elif Board[i][j] == '.':
            if i == N-1 or i == 0 or j == M-1 or j== 0:
                exit_idx.append((i, j))
        else:
            pass
# print(visited)
# print(fire_idx)
# print(exit_idx)

Q = deque([start])
while Q:
    ni, nj, ns = Q.popleft()
    if (ni, nj) in exit_idx:
        print(ns+1)
        quit(0)

    a = len(fire_idx)
    for _ in range(a):
        fire = fire_idx.popleft()
        for k in range(4):
            fi = fire[0] + dx[k]
            fj = fire[1] + dy[k]
            if 0<=fi<N and 0<=fj<M and visited[fi][fj] == 0:
                fire_idx.append((fi, fj))
                visited[fi][fj] = 1
    cnt = 0
    for l in range(4):
        nx = ni + dx[l]
        ny = nj + dy[l]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            Q.append((nx, ny, ns+1))
            cnt += 1
    if cnt == 0:
        continue
print('IMPOSSIBLE')