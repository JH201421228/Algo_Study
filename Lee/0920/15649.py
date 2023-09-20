n, r = 8, 8
arr = list(range(1, n+1))
temp = []
visited = [0]*(n+1)
def perm():
    if len(temp) == r:
        print(*temp)
        return
    for i in arr:
        if visited[i] == 0:
            visited[i] = 1
            temp.append(i)
            perm()
            visited[i] = 0
            temp.pop()
perm()