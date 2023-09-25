from collections import deque
N = int(input())
arr = [-1 for _ in range(N + 1)]
cnt = 0
arr[N] = 0
Q = deque([N])
while Q:
    now = Q.popleft()
    if now%3 == 0:
        Q.append(now//3)
        if arr[now//3] == -1:
            arr[now//3] = arr[now] + 1

    if now%2 == 0:
        Q.append(now//2)
        if arr[now // 2] == -1:
            arr[now // 2] = arr[now] + 1
    Q.append(now-1)
    if arr[now-1] == -1:
        arr[now-1] = arr[now] + 1
    if arr[1] != -1:
        break
print(arr[1])