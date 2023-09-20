from collections import deque
import sys
sys.stdin = open('supply_routes.txt')

# 델타 탐색
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    Board = [list(map(int, input())) for _ in range(N)]
    visited = [[-1] * N for _ in range(N)]
    Q = deque([(0, 0)])
    visited[0][0] = 0

    while Q:
        i, j = Q.popleft()
        # 도달했다 하여도 경로가 여러개일 수 있기 때문에 계속 진행(끝까지)
        if i == N - 1 and j == N - 1:
            continue
        # 현재 위치의 복구 시간
        cur = visited[i][j]
        for k in range(4):
            nx = i + dy[k]
            ny = j + dx[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            # 여태 방문한 적 없거나 방문한 적 있어도 내 새로운 루트의 누적값이 더 작은 경우 -> 방문
            if visited[nx][ny] == -1 or cur + Board[nx][ny] < visited[nx][ny]:
                visited[nx][ny] = cur + Board[nx][ny]
                Q.append((nx, ny))
    print(f'#{tc}', visited[N-1][N-1])