'''
문제구상
1. dfs로 연결된 노드 갯수 탐색
2. dfs + 재귀함수 이용
'''
def dfs(s):
    global count
    visited.append(s)
    for next_node in graph[s]:
        if next_node not in visited:
            count += 1
            dfs(next_node)

v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):                          #무방향 그래프 임으로 graph[b].append(a)도 추가
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = []
visited = []
count = 0
dfs(1)
print(count)







