from collections import deque

N, K = map(int, input().split())
result = 0

# N 위치좌표가 K보다 크거나 같다면 x-1로 N-K번 이동
if N >= K:
    result = N-K
else:
    # 방문 좌표 담을 coord
    coord = set()
    q = deque()
    q.append([N, 0])
    coord.add(N)

    while True:
        x, y = q.popleft()
        # x가 K의 좌표일때 break
        if x == K:
            result = y
            break
        nx = x
        # x*2 좌표로 이동하는 데 시간 0초이므로 먼저 범위 내 모두 체크
        while True:
            dx = nx * 2
            if 0 < dx <= 100000 and dx not in coord:
                q.append([dx, y])
                coord.add(dx)
                nx = nx * 2
            else:
                break
        # x*2 체크 후 x-1, x+1 확인
        for i in [-1, 1]:
            dx = x + i
            dy = y + 1
            # 좌표 범위 내 있으면서 방문한 좌표가 아니라면
            if 0 <= dx <= 100000 and dx not in coord:
                # [x+1, x-1 좌표, 시간] q에 넣기
                q.append([dx, dy])
                # 방문 체크
                coord.add(dx)

print(result)