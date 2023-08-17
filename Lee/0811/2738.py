N, M = map(int, input().split())
Board1 = [list(map(int, input().split())) for _ in range(N)]
Board2 = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        Board1[i][j] += Board2[i][j]
for i in range(N):
    print(*Board1[i])