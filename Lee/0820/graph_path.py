import sys

sys.stdin = open('graph_path.txt')

def DFS(S, G):
    stack = [S]
    visited = [0]*(V+1)
    while stack:
        now = stack.pop()
        if visited[now] == 0:
            visited[now] = 1

        for next in range(V+1):
            if Board[now][next] == 1 and visited[next] == 0:
                stack.append(next)
                if next == G:
                    return 1
    return 0


Testcase = int(input())
for test in range(Testcase):
    V, E = map(int, input().split())
    Board = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        i, j = map(int, input().split())
        Board[i][j] = 1
    S, G = map(int, input().split())

    print(f'#{test+1}', DFS(S, G))