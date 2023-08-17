n, m = map(int, input().split())    # 도착 위치
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]      # 상하좌우

def bfs(x, y):          # x, y = 시작위치
    q = []              # 큐 생성
    q.append((x, y))    # 큐에 좌표 저장
    while q:
        x, y = q.pop(0) # 좌표를 꺼낸다
        for i in range(4):  # 델타탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:  # 범위 넘어가면 스킵
                continue

            if graph[nx][ny] == 0:  # 벽을 만나도 스킵
                continue

            if graph[nx][ny] == 1:  # 1 즉 갈수 있는 곳
                graph[nx][ny] = graph[x][y] + 1 # 앞에 발판의 숫자 +1
                q.append((nx, ny))  # 이동한 위치 큐에 저장

    return graph[n-1][m-1]  # 도착 위치 발판 숫자 return

print(bfs(0, 0))

# 그래프 검증용
# for i in graph:
#     for j in i:
#         print(j, end=' ')
#     print()