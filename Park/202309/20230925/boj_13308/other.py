import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

# dijkstra : 현재 정점이 idx, 현재 단위 비용이 cost일 때 n번째 정점까지 가기 위해 드는 최소 비용을 리턴하는 함수
def dijkstra():
    inf = 98765432109876543210
    # d : 상태 공간 배열
    d = [[inf] * (max(arr) + 1) for _ in range(n + 1)]
    q = []
    d[1][arr[1]] = 0
    heapq.heappush(q, (0, arr[1], 1))
    while q:
        # now_dist : 현재 드는 총 비용
        # now_cost : 현재 정점에서 다른 정점으로 갈 때 드는 단위 비용
        # now : 현재 정점
        now_dist, now_cost, now = heapq.heappop(q)
        # 도착 시 정답 리턴
        if now == n:
            return now_dist
        if d[now][now_cost] < now_dist:
            continue
        for (next, next_dist) in adj[now]:
            # next_cost : 다음 정점으로 도착해서 쓸 단위 비용
            next_cost = min(arr[next], now_cost)
            # 현재 총 비용이 다음 정점으로 가기 위해 드는 비용보다 작다면 우선순위 큐에 삽입
            if d[next][now_cost] > now_dist + now_cost * next_dist:
                d[next][now_cost] = now_dist + now_cost * next_dist
                heapq.heappush(q, (now_dist + now_cost * next_dist, next_cost, next))


# 입력부
n, m = map(int, sys.stdin.readline().split())
arr = [-1] + list(map(int, sys.stdin.readline().split()))
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

# 정답 출력
print(dijkstra())