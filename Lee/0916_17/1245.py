import sys
sys.stdin = open('1245.txt')
input = sys.stdin.readline

# 델타 탐색 (다이얼 12369874 순서)
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

# 어떤 점을 기준으로 그 점 주변에 더 큰 위치가 있는지 확인
def check_high(i, j, Board):


N, M = map(int, input().split())
Board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 0

# 언덕이 되는 조건 : 주변에 큰 숫자가 있으면 안됨
# 주변에 같은 숫자가 있으면 그 주변에도 있으면 안됨

for i in range(N):
    for j in range(M):

