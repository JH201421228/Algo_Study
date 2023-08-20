'''
문제구상
1. bfs로 visited 배열에 +1씩 누적 시키기
'''
from collections import deque
def dfs(i,j,Arr):
    stack = []
    stack.append((i,j))
    while stack:
        now_i, now_j = stack.pop()
        for di,dj in (0,1),(1,0),(0,-1),(-1,0):
            ni = now_i + di
            nj = now_j + dj
            if 0<= ni < N and 0<= nj < M and Arr[ni][nj] == 1:
                Arr[ni][nj] = Arr[now_i][now_j] + 1
                if ni == N-1 and nj == M -1 :
                    return Arr
                else:
                    stack.append((ni, nj))

N, M = map(int,input().split())
Arr = [list(map(int,input())) for _ in range(N)]
result = dfs(0,0,Arr)
print(result)