# dfs 기본개념 (stack 이용 DFS 코드 기억해 둘것)

def dfs(graph, start, visited):
    stack = [start]
    visited[start] = True

    while stack:
        value = stack.pop()
        if not visited[value]:
            visited[value] = True
        for i in graph[value]:
            if not visited[i]:
                stack.append(i)

for _ in range(10):
    tc, n = map(int, input().split())

    arr = list(map(int, input().split()))

    graph = [[] for _ in range(101)]

    for i in range(n):
        graph[arr[i*2] + 1].append(arr[i*2 + 1] + 1)

    # print(graph)
    visited = [False] * 101
    dfs(graph, 1, visited)

    ans = 1
    if not visited[100]:
        ans = 0

    print(f'#{tc} {ans}')