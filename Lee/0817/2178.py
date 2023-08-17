# 델타 탐색 (우 하 좌 상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def min_dfs():
    stack = [(0,0)]


Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())
    # 왼쪽 위에서 출발하여 오른쪽 아래에 도달할 때 까지 이동 횟수를 세자
    # 1을 타고 이동하며 시작과 끝까지도 카운트를 해줘야 한다.
    # 인덱스 적으로는 (0,0)에서 출발하여 (N-1, M-1)에 도달
    # 항상 도착 위치로 이동할 수 있는 경우만 입력으로 주어진다.
    Board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 1 # 한 칸 이동할 때마다 1증가시킬 것
