import sys
import heapq

sys.stdin = open('1753.txt')
input = sys.stdin.readline
'''
heapq란?
우리가 아는 Queue에 오름차순 정렬 기능을 추가한 것
순서쌍을 넣게 되면 앞쪽부터 비교한다.
'''

'''
다익스트라란?
최단 경로를 검색할 때 주로 사용하는 알고리즘으로
시작 노드를 기준으로 한 번에 갈 수 있는 경로의 정보를
큐에 추가하고 (비용, 노드)
최종 리스트에 해당하는 비용을 적는다.
이때, 한 번에 갈 수 없는 경로를 만난다면 무한으로 설정한다.

이후, 큐에 들어있는 노드들 중에서 최소 비용 노드를
pop 하여 다시 갈 수 있는 노드의 정보를 기록한다.
-> 그러므로 힙큐를 통해 최소 비용 노드가 앞에오도록 설정한 것이며
순서쌍을 입력할 때, (비용, 노드번호)의 순으로 적는다.

이 때 이미 최종리스트에 숫자가 기입되어 있더라도 내가 이후 찾은 경로랑
비교하여 최솟값으로 최신화 시켜준다. -> 이 때문에 최초에 전부 무한으로 설정해둔 것
'''


def dijkstra(S):
    Q = []
    heapq.heappush(Q, (0, S))
    Final[S] = 0

    while Q:
        dist, now = heapq.heappop(Q)
        # 유망성 조사 : 이미 방문했던 곳에 거리가 더 짧았다면 그 경로는 탐색 중단
        # if Final[now] < dist:
        #     continue
        # 갈 수 있는 점들을 분석하며 그 점까지의 거리를 계산
        for next in Adj[now]:
            current_dist = Final[now] + next[1]
            # 새로 계산한 거리가 기존 적혀있던 거리보다 더 작다면 갱신하고 루트에 추가
            if current_dist < Final[next[0]]:
                Final[next[0]] = current_dist
                heapq.heappush(Q, (current_dist, next[0]))
    return


# 노드와 간선의 개수
V, E = map(int, input().split())
S = int(input())
# 연결 정보
Adj = [[] * (V + 1) for _ in range(V + 1)]
# 최대한 큰 수를 표현 그 이유는 아래에서의 무한 개념을 위함
INF = 3000000
Final = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    Adj[u].append((v, w))
# print(Adj)

dijkstra(S)

# print(Final)
for i in range(1, V + 1):
    if Final[i] == INF:
        print('INF')
    else:
        print(Final[i])
