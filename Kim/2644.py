def bfs(s, e):
    q = [s]
    visited[s][0] = True
    flag = False
    while q:
        v = q.pop(0)
        for i in graph[v]:
            temp = visited[v][1]
            if not visited[i][0] and visited[i][1] != e:
                visited[i][1] = visited[v][1] + 1
                q.append(i)
                visited[i][0] = True
            if i == e:
                flag = True
                visited[i][1] = visited[v][1] + 1
                return (flag,visited[i][1])
    return (flag, visited[e][1])

n = int(input())
a, b = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)

# print(graph)
visited = [[False, 0] for _ in range(n+1)]

flag, ans = bfs(a, b)
# print(visited)

if flag:
    print(ans)
else:
    print(-1)