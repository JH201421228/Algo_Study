import heapq
import sys
sys.stdin = open('sw_2.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dijkstra(i, j):
    visited = [[INF]*(N) for _ in range(N)]
    HQ = []
    heapq.heappush(HQ, (0, i, j))
    while HQ:
        dist, ni, nj = heapq.heappop(HQ)
        if visited[ni][nj] >= dist:
            for k in range(4):
                nx = ni + dx[k]
                ny = nj + dy[k]
                if 0<=nx<N and 0<=ny<N:
                    climb = max(0, Board[nx][ny]- Board[ni][nj])
                    gas = climb + 1 + dist
                    if gas < visited[nx][ny]:
                        heapq.heappush(HQ, (gas, nx, ny))
                        visited[nx][ny] = gas
    return visited[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    INF = 1e9
    Board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', dijkstra(0, 0))
