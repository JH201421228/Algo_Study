def dfs(n, v, g):
    v[n] = True
    for j in g[n]:
        if not v[j]:
            v[j] = True
            dfs(j, v, g)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
# print(graph)
cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i, visited, graph)
        cnt += 1

print(cnt)