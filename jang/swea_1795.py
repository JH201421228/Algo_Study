import heapq

T = int(input())
for t in range(T):
    N, M, X = map(int, input().split())
    lst = [[] for _ in range(N + 1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        lst[x].append((y, c))

    go = [0] * (N + 1)
    res = 0

    for i in range(1, N + 1):
        dist = [float('inf')] * (N + 1)
        dist[i] = 0
        q = []
        heapq.heappush(q, (0, i))

        while q:
            distance, coord = heapq.heappop(q)

            if dist[coord] < distance:
                continue
            for l in lst[coord]:
                if dist[l[0]] > distance + l[1]:
                    dist[l[0]] = distance + l[1]
                    heapq.heappush(q, (distance + l[1], l[0]))
        if i == X:
            back = dist
        else:
            go[i] = dist[X]

    for i in range(1, N + 1):
        if res < go[i] + back[i]:
            res = go[i] + back[i]

    print(f'#{t+1}', res)