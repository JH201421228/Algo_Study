import sys

sys.stdin = open('13023.txt')

def DFS(start, depth):
    global flag
    visited[start] = 1
    if depth == 5:
        flag = True
        return
    for i in range(N):
        if adj[start][i] == 1 and visited[i] == 0:
            DFS(i, depth + 1)
    visited[start] = 0


N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]
flag = False
visited = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

for i in range(N):
    DFS(i, 1)
    if flag:
        print(1)
        break
else:
    print(0)
