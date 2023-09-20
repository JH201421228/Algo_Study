N, M = 2, 2
Board = [[0] * M for _ in range(N)]

# (0, 0)부터 왼쪽부터 오른쪽으로 쭉 간다음 다시 아랫줄 왼쭉부터 오른쪽 까지를 반복
def DFS(i, j):
    cnt = 0
    if j >= M:
        i += 1
        j = 0
    # 종료조건
    if i >= N:
        return 0

    # 만약 세 곳이 중 한 곳이라도 0이라면 1이 들어갈 수 있음
    if Board[i][j - 1] == 0 or Board[i - 1][j - 1] == 0 or Board[i - 1][j] == 0:
        Board[i][j] = 1
        cnt += DFS(i, j + 1) + 1        ####
        Board[i][j] = 0
    cnt += DFS(i, j + 1)                ####
    return cnt

print(DFS(0, 0) + 1)