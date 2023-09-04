from collections import deque
import sys
from pprint import pprint
sys.stdin = open('1967.txt')


def BFS(a):
    visited = [0]*(N+1)
    Queue = deque([a])
    mid = [0]*(N+1)
    while Queue:
        now = Queue.popleft()
        if visited[now] == 0:
            visited[now] = 1
        for next in range(N+1):
            if Adj[now][next] != 0 and visited[next] == 0:
                Queue.append(next)
                mid[next] = mid[now] + Adj[now][next]
    return mid


N = int(input())
Adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(N-2):
    a, b, c = map(int, input().split())
    Adj[a][b] = c
    Adj[b][a] = c

a, b, c = map(int, input().split())
Adj[a][b] = c
Adj[b][a] = c
leaf = list(range(a+1, N+1))
pprint(Adj)
print(leaf)
final = 0
for i in leaf:
    print(BFS(i))