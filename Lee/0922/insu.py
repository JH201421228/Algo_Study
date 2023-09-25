import heapq
import sys
sys.stdin = open('insu.txt')
input = sys.stdin.readline

def dijkstra(s, g):
    visited = [INF]*(N+1)
    visited[s] = 0
    HQ = []
    heapq.heappush(HQ,(0, s))
    while HQ:
        dist, now = heapq.heappop(HQ)
        if visited[now] < dist:
            continue

        for next in adj[now]:
            cur_dist = visited[now] + next[0]
            if cur_dist < visited[next[1]]:
                visited[next[1]] = cur_dist
                heapq.heappush(HQ, (cur_dist, next[1]))
    return visited[g]


INF = 1e9
T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    final = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        adj[a].append((c, b))
    for i in range(1, N+1):
        mid = dijkstra(i, X) + dijkstra(X, i)
        if final<mid:
            final = mid
    print(f'#{tc}', final)