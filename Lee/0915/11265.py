import heapq
import sys

sys.stdin = open('11265.txt')
input = sys.stdin.readline


def dijkstra(n, m):
    final = [INF] * (V + 1)
    final[n] = 0
    Q = []
    heapq.heappush(Q, (0, n))
    while Q:
        dist, now = heapq.heappop(Q)
        if final[now] < dist:
            continue
        for next in range(V):
            current = final[now] + Adj[now][next]
            if current < final[next]:
                final[next] = current
                heapq.heappush(Q, (current, next))
    return final[m]


V, E = map(int, input().split())
Adj = [list(map(int, input().split())) for _ in range(V)]
print(Adj)
INF = 10 ** 9
for _ in range(E):
    a, b, c = map(int, input().split())




    time = dijkstra(a - 1, b - 1)
    if time > c:
        print('Stay here')
    else:
        print('Enjoy other party')
