from collections import deque
import sys
sys.stdin = open('a.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
Board = [list(map(int, input())) for _ in range(N)]

S = (0, 0)
G = (N-1, M-1)
visited = [[0]*M for _ in range(N)]
def BFS(S, G):
    Queue = deque([S])
    visited[S[0]][S[1]] = 1
    while Queue:
        now = Queue.popleft()
        for k in range(4):
            ni = now[0] + dx[k]
            nj = now[1] + dy[k]
            if 0 <= ni < N and 0 <= nj < M and Board[ni][nj] == 1 and visited[ni][nj] == 0:
                Queue.append((ni, nj))
                visited[ni][nj] = visited[now[0]][now[1]] + 1
                if ni == N-1 and nj == M-1:
                    return visited[ni][nj]

print(BFS(S, G))