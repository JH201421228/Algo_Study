import sys
sys.stdin = open('14503.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
# r, c 좌표 / d : 방향(0북/1동/2남/3서) 12시부터 시계방향
r, c, d = map(int, input().split())
Board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

def check(i, j):
    for k in range(4):
        di = i + dx[k]
        dj = j + dy[k]
        if di<0 or di>=N or dj<0 or dj>=M:
            continue
        if Board[di][dj] == 0:
            return True
    return False



stack = [(r, c)]
while stack:
    ni, nj = stack.pop()
    if Board[ni][nj] == 0:
        Board[ni][nj] = 2
        cnt += 1

    if not check(ni, nj):
        ni -= dx[d]
        nj -= dy[d]
        if ni<0 or ni>=N or nj<0 or nj>=M or Board[ni][nj]==1:
            print(cnt)
            quit(0)
        else:
            stack.append((ni, nj))
    else:
        d = (d-1) % 4
        while Board[ni+dx[d]][nj+dy[d]] != 0:
            d = (d-1)%4
        stack.append((ni+dx[d], nj+dy[d]))