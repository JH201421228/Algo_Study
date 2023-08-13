N, M = map(int, input().split())
nx, ny = map(int, input().split())
move = int(input())

# 우상 / 좌상 / 좌하 / 우하
dx = [1, -1, -1, 1]
dy = [1, 1, -1, -1]
k = 0
for _ in range(move):
    nx += dx[k%4]
    ny += dy[k%4]
    if (0 <= nx <= N) and ny > N:
        k += 3
        nx += dx[k%4]-dx[k-3]
        ny += dy[k%4]-dx[k-3]
    elif (0 <= nx <= N) and ny < 0:


print(nx, ny)