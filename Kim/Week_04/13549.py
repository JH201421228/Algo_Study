from collections import deque
n, k = map(int, input().split())

q = deque()
q.append(n)
visited = [-1 for _ in range(100001)]   # 시작지점의 횟수를 0으로 잡기 위해 -1로 초기화
visited[n] = 0                          # 시작지점 = 0

while q:
    v = q.popleft()                     # BFS (최소 횟수)
    if v == k:                          # 꺼낸 숫자 == 도착 지점 (방문했을때 있는 값이 최소값)
        print(visited[v])
        break

    if 0 <= v-1 < 100001 and visited[v-1] == -1:
        visited[v-1] = visited[v] + 1
        q.append(v-1)

    if 0 <= v*2 < 100001 and visited[v*2] == -1:
        visited[v*2] = visited[v]
        q.appendleft(v*2)               # X2인 경우가 최소 시간이니까 우선순위 앞 (appendleft)

    if 0 <= v+1 < 100001 and visited[v + 1] == -1:
        visited[v+1] = visited[v] + 1
        q.append(v+1)