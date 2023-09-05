from collections import deque

# 현재 위치와 목표 위치 입력
n, k = map(int, input().split())
visited = [False] * 100001
q = deque()
# 시작 위치와 움직인 시간을 입력
q.append([n, 0])

min_count = 1000000

# BFS로 전수조사하며 이동
while q:
    cur, count = q.popleft()
    visited[cur] = True
    # 방문했다면 작은 애를 선정
    if cur == k:
        min_count = min(min_count, count)

    # 이동 방법은 3가지로(좌 / 우 / 2배)
    if 0 <= cur + 1 < 100001 and not visited[cur + 1]:
        q.append([cur + 1, count + 1])
    if 0 <= cur - 1 < 100001 and not visited[cur - 1]:
        q.append([cur - 1, count + 1])
    if 0 <= cur * 2 < 100001 and not visited[cur * 2]:
        q.append([cur * 2, count])      # 2배할 때는 시간을 올리지는 않음

print(min_count)