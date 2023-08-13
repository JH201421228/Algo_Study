import sys
sys.stdin = open('a.txt')
from pprint import pprint

T = int(input())
# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    P = 2
    ni, nj = 0, 0
    k = 0
    arr[0][0] = 1
    while P != N**2 + 1:
        ni += di[k % 4]
        nj += dj[k % 4]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            arr[ni][nj] = P
            P += 1
        else:
            ni -= di[k % 4]
            nj -= dj[k % 4]
            k += 1

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])