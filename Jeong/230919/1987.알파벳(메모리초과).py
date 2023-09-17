'''
설계
1. bfs로 최대 깊이 찾기
2. deque에 집어넣을때 알파벳까지 같이 집어 넣어서 순회가능여부 검사하기
3. 어짜피 이미 지나온 경로는 deque 3번째 인자에 포함이 되기 때문에 왔던 곳을 다시 재방문 할 일이 없음
4. 대신 같은 격자에 대해 경로가 다를 수 있으므로 최대 거리로 최신화 하기
'''

def bfs(i,j,k):
    q = deque([(i,j,k)])
    depth[i][j] = 1

    while q:
        ci, cj, ck = q.popleft()
        for di,dj in (0,1),(1,0),(0,-1),(-1,0):
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < R and 0 <= nj < C:
                if Arr[ni][nj] not in ck:
                    depth[ni][nj] = max(depth[ni][nj], depth[ci][cj] + 1)
                    nk = list(set(ck + [Arr[ni][nj]]))
                    q.append((ni,nj,nk))

import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())
Arr = []
depth = [[0] * C for _ in range(R)]
for _ in range(R):
    Arr.append(input().rstrip())

bfs(0,0,[Arr[0][0]])
result = 0
for row in depth:
    result = max(result,max(row))

print(result)