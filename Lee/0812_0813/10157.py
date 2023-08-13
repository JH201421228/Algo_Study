from pprint import pprint
# C : 가로, R : 세로 이며 아래왼쪽이 (1, 1)
C, R = map(int, input().split())
N = int(input())

Board = [[0] * C for _ in range(R)]

# 델타 탐색을 위한 방향(위, 오른, 아래, 왼) 의 반복
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 보드를 순회하며 시작점부터 움직이기 시작할 것
# 어떻게 회전을 표할 것이냐 사실 가로 세로가 정해져있기 때문에 for문으로 가능하나
# 벽을 만나면 회전하는 것으로 구현하자

k = 0
p = 1
Board[R-1][0] = p
nx = R - 1
ny = 0
while p != C * R:
    nx += dx[k % 4]
    ny += dy[k % 4]
    if 0 <= nx < R and 0 <= ny < C and Board[nx][ny] == 0:
        p += 1
        Board[nx][ny] = p

    else:
        nx += dx[(k + 2) % 4]
        ny += dy[(k + 2) % 4]
        k += 1

a = 0
b = 0
for i in range(R):
    for j in range(C):
        if Board[i][j] == N:
            a = R - i
            b = j + 1

if a==0 and b==0:
    print(0)
else:
    print(b, a)