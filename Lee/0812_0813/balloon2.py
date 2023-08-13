import sys
sys.stdin = open('input1 (1).txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    final = 0

    for i in range(N):
        for j in range(M):
            mid = Board[i][j]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if (0 <= nx < N) and (0 <= ny < M):
                    mid += Board[nx][ny]
            if mid >= final:
                final = mid
    print(f'#{test+1}', final)