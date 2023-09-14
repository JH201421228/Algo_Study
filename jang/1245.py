import sys
from collections import deque
direct = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
N, M = map(int, sys.stdin.readline().strip().split())
MAP = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if v[i][j] == 0:
            flag = 1
            q = deque()
            for k in range(8):
                di = i + direct[k][0]
                dj = j + direct[k][1]
                if 0 <= di < N and 0 <= dj < M:
                    if MAP[i][j] < MAP[di][dj]:
                        flag = 0
                        break
                    elif MAP[i][j] == MAP[di][dj]:
                        q.append((di, dj))
            # 산봉우리가 맞다면 인접한 곳 조사
            if flag:
                while q and flag:
                    x, y = q.popleft()
                    for k in range(8):
                        dx = x + direct[k][0]
                        dy = y + direct[k][1]
                        if 0 <= dx < N and 0 <= dy < M:
                            if MAP[x][y] < MAP[dx][dy]:
                                flag = 0
                                break
                            elif MAP[x][y] == MAP[dx][dy] and v[dx][dy] == 0:
                                q.append((dx, dy))
                    v[x][y] = 1
            result += flag

print(result)