def dfs(x):
    global result
    if v[x] >= 5:
        result = 1
        return
    for l in lst[x]:
        if v[l] == 0:
            v[l] = v[x] + 1
            dfs(l)
            v[l] = 0


N, M = map(int, input().split())
lst = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
result = 0
v = [0] * N
for i in range(N):
    v[i] = 1
    dfs(i)
    v[i] = 0

print(result)
