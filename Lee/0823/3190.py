from collections import deque
import sys
sys.stdin = open('a.txt')

# 판 크기랑 사과 개수 입력
N = int(input())
App = int(input())
# 판 입력받기
Board = [[0]*(N+1) for _ in range(N+1)]
# 사과 심기
for _ in range(App):
    a, b = map(int, input().split())
    Board[a][b] = 1
R = int(input())
# 방향 전환 시간과 방향
dir_n = []
dir_lr = []
for _ in range(R):
    a, b = input().split()
    dir_n.append(int(a))
    dir_lr.append(b)

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

Board[1][1] = 2
start = (1, 1)
k = 0
time = 0
Queue = deque()

def move(start):
    global time
    global k
    stack = [start]
    while stack:
        time += 1
        now = stack.pop()
        Queue.append(now)
        ni = now[0] + dx[k%4]
        nj = now[1] + dy[k%4]
        # 사과 확인 / 벽 확인 / 자기 몸 확인 / 방향전환 확인
        if 0<ni<N+1 and 0<nj<N+1:
            stack.append((ni, nj))
            if Board[ni][nj] == 0:
                Board[ni][nj] = 2
                a, b = Queue.popleft()
                Board[a][b] = 0
            elif Board[ni][nj] == 2:
                return time
            elif Board[ni][nj] == 1:
                Board[ni][nj] = 2
        else:
            return time

        if dir_n:
            if time == dir_n[0] and dir_lr[0] == 'L':
                k -= 1
                dir_n.pop(0)
                dir_lr.pop(0)

            elif time == dir_n[0] and dir_lr[0] == 'D':
                k += 1
                dir_n.pop(0)
                dir_lr.pop(0)
    return
print(move(start))