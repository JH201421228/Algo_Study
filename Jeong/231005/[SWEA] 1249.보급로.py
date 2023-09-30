'''
설계
1. BFS로 최단거리 구하기
2. BFS시간초과 뜨면 다익스트라로 최단경로만 찾아서 가도 될듯?
'''

from collections import deque

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    Arr = [list(map(int,input())) for _ in range(N)]
    dist = [[int(1e9)]*N for _ in range(N)]
    q = deque([(0,0)])
    dist[0][0] = 0

    while q:
        i,j = q.popleft()

        for di,dj in (0,1),(1,0),(-1,0),(0,-1):
            ni,nj = i+di,j+dj
            if 0<=ni<N and 0<=nj<N:
                if dist[ni][nj] > dist[i][j]+Arr[ni][nj]:
                    dist[ni][nj] = dist[i][j]+Arr[ni][nj]
                    q.append((ni,nj))

    res = dist[-1][-1]
    print(f'#{test_case} {res}')
