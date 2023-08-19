f, s, g, u, d = map(int, input().split())
graph = [[] for _ in range(f + 1)]
for i in range(1, f + 1):
    if i - d > 0:
        graph[i].append((i-d))
    if i + u <= f:
        graph[i].append((i+u))
visited = [[False, 0] for _ in range(f+1)]
# print(graph)


def bfs(s):
    q = [s]
    visited[s][0] = True
    while q:
        v = q.pop(0)
        for i in graph[v]:
            if not visited[i][0]:
                visited[i][1] = visited[v][1] + 1
                q.append(i)
                visited[i][0] = True

bfs(s)

if visited[g][0]:
    print(visited[g][1])
elif not visited[g][0]:
    print('use the stairs')