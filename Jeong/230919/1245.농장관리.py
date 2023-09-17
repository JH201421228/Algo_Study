'''
설계
1. 한 격자를 기준으로 각 상하좌우를 뺄 때마다 뺀 값이
    (1) 양수 : 산봉우리 가능성 ↑
    (2) 음수 : 산봉우리 탈락 → flag -> False로
    (3) 0 : 산봉우리와 같은 높이 -> 해당 부분도 연결 시켜 같이 산봉우리인지 확인 진행

2. 전체 순회를 하는데 이미 방문한 격자는 방문 처리
    (0) 이미 방문 한거는 검사 대상에는 들어오고 방문 대상에는 제외 해야됨
        - 검사 : 현재 방문한 봉우리 기준 인접한 부분과 높이차이 검사


3. dfs 도중 산봉우리가 아님을 발견하더라도 함수 전체를 종료 시키면 안되고
방문하던 격자는 다 방문을 진행하고 나와야 됨 -> 이렇게 안하면 이후 인접한 격자가 최초방문되어 로직이 이상하게 돌아감
'''
def dfs(i,j,now):
    global flag
    visited[i][j] = 1
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1,1), (1,-1), (-1,-1), (-1,1):
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < M:
            check = Arr[ni][nj]

            if now - check < 0:
                flag = False

            elif now - check == 0 and not visited[ni][nj]:
                dfs(ni,nj,check)

import sys
N, M = map(int,input().split())
input = sys.stdin.readline
Arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        now = Arr[i][j]
        flag = True
        if not visited[i][j] and now > 0:
            dfs(i,j,now)
            if flag == True:
                cnt += 1
print(cnt)