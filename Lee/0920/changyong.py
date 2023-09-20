import sys
sys.stdin = open('changyong.txt')

def DFS(node):
    global cnt
    stack = [node]
    visited[node] = 1
    while stack:
        now = stack.pop()
        for nex in adj[now]:
            if visited[nex] == 0:
                stack.append(nex)
                visited[nex] = 1
    cnt += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    cnt = 0
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    for i in range(1, N+1):
        if visited[i] == 0:
            DFS(i)
    print(f'#{tc}', cnt)