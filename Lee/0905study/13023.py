import sys
sys.stdin = open('13023.txt')

def DFS(node, visited):
    visited.add(node)
    # 종료 조건을 입력하고 재귀를 돌 것이므로 강제 종료를 시킴
    if len(visited) == 5:
        print(1)
        exit(0)
    for next in range(N):
        if adj[node][next] == 1 and next not in visited:
            DFS(next, set(visited))

# 노드의 개수와 간선의 개수를 입력 받는다.
N, M = map(int, input().split())
# 인접행렬에 정보 기입
adj = [[0]*N for _ in range(N)]
for m in range(M):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

# DFS를 통해 0번부터 DFS를 실행하며 5인 길이가 나오는지 확인한다.
for i in range(N):
    DFS(i, set())    # visited 용도로 set() 사용
print(0)    # 강제 종료가 안되면 0을 출력