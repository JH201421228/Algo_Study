def dfs(start, visited):
    visited[start] = True       # 최초 방문 노드 방문 처리
    for i in graph[start]:      # 방문한 노드에서 갈수 있는 노드
        if not visited[i]:      # 방문안한 노드가 있다면
            dfs(i, visited)     # dfs로 방문... (재귀)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(int(input())):       # 양방향 인접리스트 생성
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
v = [False] * (n + 1)       # 컴퓨터 1부터 저장하기위해 +1
dfs(1, v)                   # 1번부터 시작

print(v)
print(v[2:].count(True))    # 1번에 의해 감염되는 컴퓨터 수
print(graph)
'''
0 0 0 1 1 0
1 0
'''