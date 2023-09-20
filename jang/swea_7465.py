from collections import deque


# bfs 돌면서 연결된 사람들 방문
def bfs(n):
    q = deque()
    q.append(n)
    v[n] = 1
    while q:
        num = q.popleft()
        for l in lst[num]:
            if v[l] == 0:
                v[l] = n
                q.append(l)


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    lst = [[] for _ in range(N+1)]
    v = [0] * (N+1)

    # 양방향 인접리스트
    for i in range(M):
        x, y = map(int, input().split())
        lst[x].append(y)
        lst[y].append(x)

    res = 0
    for i in range(1, N+1):
        # 아직 방문하지 않은 lst[i] 일 때만 조사, 조사할때마다 res += 1 (무리 + 1)
        if v[i] == 0:
            bfs(i)
            res += 1

    print(f'#{t+1}', res)