import sys
sys.stdin = open('13023.txt')

def DFS(node, cnt, visited):
    visited.add(node)
    if len(visited) == 5:
        print(1)
        exit(0)
    for next in range(N):
        if adj[node][next] == 1 and next not in visited:
            DFS(next, cnt+1, set(visited))


N, M = map(int, input().split())
adj = [[0]*N for _ in range(N)]
for m in range(M):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1
for i in range(N):
    DFS(i, 1, set())
print(0)