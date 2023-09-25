import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def odinson(start):
    distance = [float('inf')] * (N+1)
    pq = [(0, start)]
    distance[start] = 0
    multi = cost[start-1]

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next, weight in graph[now]:
            if distance[next] > dist + weight * multi:
                distance[next] = dist + weight * multi
                heapq.heappush(pq, (dist + weight * multi, next))
    return distance


def dua_lipa(row, val):
    global ans

    if row == N-1:
        if val < ans:
            ans = val
        return

    if val > ans:
        return

    for idx in range(row, N):
        if not visited[idx]:
            visited[idx] = 1
            dua_lipa(idx, val + for_ans[row][idx])
            visited[idx] = 0


N, M = map(int, input().split())
cost = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    p1, p2, point = map(int, input().split())
    graph[p1].append((p2, point))
    graph[p2].append((p1, point))
# print(graph)
for_ans = []
for num in range(1, N+1):
    for_ans.append(odinson(num)[1:])

visited = [0] * N
visited[0] = 1
ans = float('inf')
dua_lipa(0, 0)
print(ans)
# for inner in for_ans:
#     print(inner)
