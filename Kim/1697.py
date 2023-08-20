n, k = map(int, input().split())

graph = [[] for _ in range(100001)]
for i in range(100001):
    if (i * 2) < 100001:
        graph[i].append(i*2)
    if i + 1 < 100001:
        graph[i].append(i+1)
    if i - 1 >= 0:
        graph[i].append(i-1)

q = [n]
visited = [[False, 0] for _ in range(100001)]
while not visited[k][0]:
    visited[n][0] = True
    while q:
        v = q.pop(0)
        for i in graph[v]:
            if not visited[i][0]:
                visited[i][0] = True
                visited[i][1] = visited[v][1] + 1
                q.append(i)

        if visited[k][0]:
            break

print(visited[k][1])