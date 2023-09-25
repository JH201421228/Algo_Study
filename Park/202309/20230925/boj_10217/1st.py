import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def KCM():
    pq = [(0, 0, 1)]
    time_line = [[float('inf') for _ in range(M+1)] for _ in range(N+1)]
    time_line[1][0] = 0

    while pq:
        time, dist, now = heapq.heappop(pq)
        if time_line[now][time] < dist:
            continue
        if now == N:
            return time
        for next, weight, next_time in graph[now]:
            if next_time + time < M+1 and time_line[next][time+next_time] > dist+weight:
                time_line[next][time + next_time] = dist + weight
                heapq.heappush(pq, (next_time + time, dist + weight, next))
    return 'Poor KCM'


T = int(input())
N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(K):
    start, end, point, time = map(int, input().split())
    graph[start].append((end, point, time))
print(KCM())