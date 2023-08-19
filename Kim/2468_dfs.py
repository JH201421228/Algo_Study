N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
area = 1
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for h in range(100):
    cnt = 0
    s = []
    v = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if lst[i][j] > h and v[i][j] == 0:
                x = i
                y = j
                cnt += 1
                while True:
                    for k in range(4):
                        nx = x + di[k]
                        ny = y + dj[k]
                        if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] > h and v[nx][ny] == 0:
                            s.append([nx, ny])
                            v[nx][ny] = 1
                    else:
                        if s:
                            x, y = s.pop()
                        else:
                            break
    if area < cnt:
        area = cnt
print(area)