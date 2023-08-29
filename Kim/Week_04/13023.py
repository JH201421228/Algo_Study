import sys
input = sys.stdin.readline

def dfs(start, cnt, v):                 # DFS 백트래킹
    global flag
    if cnt == 4:                        # 깊이 4 << 1~5까지 연결 O
        flag = True                     # 성립하니까 True and return
        return

    v[start] = True                     # 최초 시작 지점 방문처리

    for j in graph[start]:              # 연결된 노드 확인
        if not v[j]:
            v[j] = True                 # 방문처리
            dfs(j, cnt + 1, v)          # 백트래킹
    v[start] = False                    # ★다 돌았는데 깊이가 4가 아니다? 젤앞 지우고 계속

n, m = map(int, input().split())        # 노드수, 간선수
graph = [[] for _ in range(n)]          # 인접리스트
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)                  # 무방향 그래프?
    graph[b].append(a)

flag = False                            # 1개라도 존재한다면? True
visited = [False] * n                   # 어디서부터 시작해서 5명?
for i in range(n):                      # 모든 케이스 검사
    dfs(i, 0, visited)
    if flag:                            # 만약 1개라도 만족하면? True and break
        break

if flag:
    print(1)
else:
    print(0)