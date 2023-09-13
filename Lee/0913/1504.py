import heapq
import sys
sys.stdin = open('1504.txt')
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

# 다익스트라에 변수는 시작점과 끝점을 넣는다.
def dijk(start, goal):
    # 한 번 돌 때마다 최단경로 리스트 초기화
    shortest = [INF]*(V+1)
    Q = []
    heapq.heappush(Q, (0, start))
    shortest[start] = 0

    while Q:
        distance, now = heapq.heappop(Q)
        # 가지치기 : 이미 방문했던 곳에 거리가 더 짧은 것이 적혀있다면 다음 진행
        if shortest[now] < distance:
            continue
        for next in Adj[now]:
            current_distance = shortest[now] + next[1]
            if current_distance < shortest[next[0]]:
                shortest[next[0]] = current_distance
                heapq.heappush(Q, (current_distance, next[0]))

    return shortest[goal]

# 노드와 간선의 개수
V, E = map(int, input().split())
# 연결 정보
Adj = [[] for _ in range(V+1)]
# 간선마다의 가중치가 있으므로 연결 정보를 튜플의 형태로 저장
for _ in range(E):
    a, b, c = map(int, input().split())
    Adj[a].append((b, c))
    Adj[b].append((a, c))
# 가야할 곳 2곳 위치
should_go1, should_go2 = map(int, input().split())
# 무한을 의미하는 수
INF = 10**9

'''
1->a->b->N으로 오거나
1->b->a->N으로 오는 것 둘 중 하나
'''
route1 = dijk(1, should_go1) + dijk(should_go1, should_go2) + dijk(should_go2, V)
route2 = dijk(1, should_go2) + dijk(should_go2, should_go1) + dijk(should_go1, V)

# 초기를 무한으로 도배했기 때문에 경로가 없다면 무한으로 내려올 것
# 둘 다 무한이 포함되어있다면 불가능한 길
if route1>=INF and route2>=INF:
    print(-1)
else:
    print(min(route1, route2))