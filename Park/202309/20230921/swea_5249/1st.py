import sys
import heapq
sys.stdin = open('input.txt')


def least_tree():
    pq = [(0, 0)]
    # distance = [float('inf') for _ in range(V+1)]
    # distance[0] = 0
    check_list = [0] * (V+1)
    ans = 0
    cnt = 0
    while pq:
        dist, now = heapq.heappop(pq)
        if cnt == V+1:
            break
        if check_list[now]:
            continue
        check_list[now] = 1
        ans += dist
        # print(ans, now)
        cnt += 1
        for next, weight in graph[now]:
            if not check_list[next]:
                heapq.heappush(pq, (weight, next))
    return ans


T = int(input())
for test in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, point = map(int, input().split())
        graph[n1].append((n2, point))
        graph[n2].append((n1, point))
    distance = [float('inf') for _ in range(V + 1)]
    print(f'#{test + 1} {least_tree()}')
    # print(sum(least_tree()))
