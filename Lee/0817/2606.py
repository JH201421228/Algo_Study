import sys
from pprint import pprint
sys.stdin = open('2606.txt')


def DFS(N):
    stack = [1]
    while stack:
        now = stack.pop()
        visited[1] = 1
        for i in range(1, N+1):
            if Board[now][i] == 1 and visited[i] == 0:
                stack.append(i)
                path.append(i)
                if visited[i] == 0:
                    visited[i] = 1

N = int(input())
connect = int(input())
Board = [[0] * (N + 1) for _ in range(N + 1)]
for cn in range(connect):
    i, j = map(int, input().split())
    Board[i][j] = 1
    Board[j][i] = 1

# pprint(Board)

path = [1]
visited = [0] * (N + 1)

DFS(N)
print(len(path) - 1)