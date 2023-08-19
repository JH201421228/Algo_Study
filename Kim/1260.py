from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

v_dfs = [False] * (n+1)
v_bfs = [False] * (n+1)


def dfs(start):             # 재귀이용
    v_dfs[start] = True
    print(start, end=' ')
    for j in graph[start]:
        if not v_dfs[j]:
            dfs(j)


def bfs(start):             # while문, 재귀 X, 큐에 계속 다음 노드 넣음
    q = deque([start])
    v_bfs[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for k in graph[v]:
            if not v_bfs[k]:
                q.append(k)
                v_bfs[k] = True

dfs(v)
print()
bfs(v)