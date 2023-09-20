from collections import deque

direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
T = int(input())
for t in range(T):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]

    # v 최댓값으로 초기화
    v = [[float('inf')] * N for _ in range(N)]
    v[0][0] = MAP[0][0]
    q = deque()
    q.append((0, 0))

    # (0, 0) 시작으로 사방 탐색
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + direct[i][0]
            dy = y + direct[i][1]
            # 원래의 v[dx][dy]값보다 (x, y)에서 출발해서 MAP[dx][dy](작업시간)에 도착하는 시간이 짧은 경우
            if 0 <= dx < N and 0 <= dy < N and v[dx][dy] > v[x][y] + MAP[dx][dy]:
                v[dx][dy] = v[x][y] + MAP[dx][dy]
                # 새로운 v[dx][dy]값으로 사방 다시 탐색하기위해 append
                q.append((dx, dy))

    res = v[-1][-1]
    print(f'#{t+1}', res)