import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def fuxking_problem():
    pq = [(0, 1, cost[0])]
    distance_matrix = [[float('inf')] * (max(cost) + 1) for _ in range(N+1)]
    distance_matrix[1][cost[0]] = 0

    while pq:
        dist, now, costs = heapq.heappop(pq)
        if distance_matrix[now][costs] < dist:
            continue
        if now == N:
            return dist
        for next, weight in graph[now]:
            next_costs = min(cost[next-1], costs)
            if distance_matrix[next][costs] > dist + costs * weight:
                distance_matrix[next][costs] = dist + costs * weight
                heapq.heappush(pq, (dist + costs * weight, next, next_costs))



N, M = map(int, input().split())
cost = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    p1, p2, point = map(int, input().split())
    graph[p1].append((p2, point))
    graph[p2].append((p1, point))
# print(graph)
print(fuxking_problem())