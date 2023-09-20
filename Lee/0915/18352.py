from collections import deque
import sys
sys.stdin = open('18352.txt')
input = sys.stdin.readline


def dijkstra(X):
    Q = deque([X])
    visited = [-1]*(N+1)
    visited[X] = 0
    while Q:
        now = Q.popleft()
        for next in Adj[now]:
            if visited[next] == -1:
                Q.append(next)
                visited[next] = visited[now] + 1
    return visited




# N(도시 개수), M(도로 개수), K(거리 정보), X(시작 번호)
N, M, K, X = map(int, input().split())
Adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    Adj[a].append(b)

# dijkstra(X) : X에서 출발하여 각 노드별 최단거리가 적힌 리스트가 나올 리스트
final_list = dijkstra(X)
if K in final_list:
    for i in range(N+1):
        if final_list[i] == K:
            print(i)
else:
    print(-1)