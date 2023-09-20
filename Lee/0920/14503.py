import sys
sys.stdin = open('14503.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
# r, c 좌표 / d : 방향(0북/1동/2남/3서) 12시부터 시계방향
r, c, d = map(int, input().split())
Board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
fi_flag = True
while fi_flag:
    cl_flag = False
    if Board[r][c] == 0:
        Board[r][c] = 2
        cnt += 1


    for k in range(4):
        dr = r + dx[k]
        dc = c + dy[k]
        if dr<0 or dr>=N or dc<0 or dc>=M:
            continue
        if Board[dr][dc] == 0:
            d = (d-1)%4
            r = dr
            c = dc
            cl_flag = True
            break
    if Board[r][c] == 0:
        continue

    if cl_flag == False:
        dr = r - dx[d]
        dc = c - dy[d]
        if 0<=dr<N and 0<=dc<M and Board[dr][dc] != 1:
            r = dr
            c = dc
        else:
            fi_flag = False
print(cnt)