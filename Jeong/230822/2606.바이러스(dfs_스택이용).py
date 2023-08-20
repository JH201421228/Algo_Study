'''
문제구상
1. dfs로 연결된 노드 갯수 탐색
2. dfs + 스택 이용
'''
def dfs(s):
    global count
    stack.append(s)
    while stack:
        check_node = stack.pop()
        for node in graph[check_node]:
            if node not in visited:
                count += 1
                visited.append(node)
                stack.append(node)
    if count == 0:                       # 만약 count == 0 이라면 -1 하지 않고 0으로 출력
        return 0

    else:
        return count - 1                  #무방향 그래프로 연결되어 for문에서 시작 컴퓨터도 무조건 포함이 됨 -> 문제 조건에 따라 시작컴퓨터는 갯수에서 제외해야 함으로 -1

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
result = dfs(1)
print(result)







