import sys
from collections import deque
direct = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
N, M = map(int, sys.stdin.readline().strip().split())
MAP = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
result = 0

# N * N 돌면서 산봉우리인지 아닌지 조사하기
for i in range(N):
    for j in range(M):

        # MAP[i][j] 아직 조사하지 않은 경우
        if v[i][j] == 0:
            flag = 1
            q = deque()
            for k in range(8):
                di = i + direct[k][0]
                dj = j + direct[k][1]
                if 0 <= di < N and 0 <= dj < M:
                    if MAP[i][j] < MAP[di][dj]:
                        # 만약 산봉우리가 아니라면
                        # flag = 0, break로 종료
                        flag = 0
                        break
                    elif MAP[i][j] == MAP[di][dj]:
                        # 인접한 곳 중 높이가 같은 곳이 있다면 q에 추가
                        q.append((di, dj))

            # MAP[i][j]가 산봉우리가 맞다면(flag == 1) 높이가 같은 인접한 곳 조사
            # 이어지는 산봉우리들이 있는지?
            if flag:
                while q and flag:
                    x, y = q.popleft()
                    for k in range(8):
                        dx = x + direct[k][0]
                        dy = y + direct[k][1]
                        if 0 <= dx < N and 0 <= dy < M:
                            # 만약 인접한 곳 중 산봉우리가 아닌 곳이 있다면
                            # flag = 0
                            if MAP[x][y] < MAP[dx][dy]:
                                flag = 0
                                break
                            elif MAP[x][y] == MAP[dx][dy] and v[dx][dy] == 0:
                                q.append((dx, dy))
                    # 인접한 곳 조사한 곳 방문처리
                    v[x][y] = 1
            # 산봉우리가 맞다면 + 1
            result += flag

print(result)