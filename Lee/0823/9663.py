N = int(input())
Board = [[0]*N for _ in range(N)]
# 상하 좌우 전부 1로 밀어버리고 대각선은?

def DFS(start):
    stack = [start]
    while stack:
        now = stack[-1]
        for i in range(N):
            Board[i][now[1]] = 1
            Board[now[0]][i] = 1
            # 이 자리에 대각선 1박는 로직 필요
        for j in range(N):
            if Board[now[0]+1][j] == 0:
                stack.append((now[0]+1, j))

    return


start = (0, 0)