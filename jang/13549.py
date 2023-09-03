from collections import deque

N, K = map(int, input().split())
result = 0
if N >= K:
    result = N-K
else:
    coord = set()
    q = deque()
    q.append([N, 0])
    coord.add(N)
    while True:
        x, y = q.popleft()
        if x == K:
            result = y
            break
        nx = x
        while True:
            dx = nx * 2
            if 0 < dx <= 100000 and dx not in coord:
                q.append([dx, y])
                coord.add(dx)
                nx = nx * 2
            else:
                break
        for i in [(-1, 1), (1, 1)]:
            dx = x + i[0]
            dy = y + i[1]
            if 0 <= dx <= 100000 and dx not in coord:
                q.append([dx, dy])
                coord.add(dx)

print(result)