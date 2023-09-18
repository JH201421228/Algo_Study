'''
설계
1. dfs로 최대 깊이 찾기
2. depth는 최댓 값만 갱신하기
3. 어짜피 이미 지나온 경로는 deque 3번째 인자에 포함이 되기 때문에 왔던 곳을 다시 재방문 할 일이 없음
'''
def dfs(i,j,k,depth):
    q = deque([(i,j,k,depth)])
    result = 1                      # 맵이 전부 같은 알파벳일 때는 결과 1 돼야됨
    while q:
        ci, cj, ck, depth = q.pop()
        for di,dj in (0,1),(1,0),(0,-1),(-1,0):
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < R and 0 <= nj < C:
                if Arr[ni][nj] not in ck:
                    result = max(result, depth+1)
                    nk = ck + Arr[ni][nj]
                    q.append((ni,nj,nk,depth+1))
    return result

import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())
Arr = []
depth = [[0] * C for _ in range(R)]
for _ in range(R):
    Arr.append(input().rstrip())

result = dfs(0,0,Arr[0][0],1)
print(result)