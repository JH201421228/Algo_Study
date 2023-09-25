import sys
import heapq
sys.stdin = open('sw_1.txt')

def prim(start):
    HQ = []
    visited = [0]*(V+1)
    heapq.heappush(HQ, (0, start))
    summ = 0
    cnt = 0
    while HQ:
        dist, now = heapq.heappop(HQ)
        if visited[now] == 0:
            summ += dist
            cnt += 1
            visited[now] = 1
            for i in adj[now]:
                if visited[i[1]] == 0:
                    heapq.heappush(HQ, i)
        if cnt == V+1:
            break
    return summ


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        adj[a].append((c, b))
        adj[b].append((c, a))

    print(f'#{tc}', prim(0))