import sys
from pprint import pprint
sys.stdin = open('2606.txt')


def DFS(N):
    stack = [1]
    while stack:    # stack에 있는동안 반복
        now = stack.pop()   # 현재위치
        visited[1] = 1      # 방문기록
        for i in range(1, N+1):
            if Board[now][i] == 1 and visited[i] == 0:
                stack.append(i)
                path.append(i)  # 경로에 추가
                if visited[i] == 0:
                    visited[i] = 1

# 연결 정보를 이중리스트에 담음
N = int(input())
connect = int(input())

Board = [[0] * (N + 1) for _ in range(N + 1)]
for cn in range(connect):
    i, j = map(int, input().split())
    Board[i][j] = 1     # 양방향이므로
    Board[j][i] = 1

# pprint(Board)

path = [1]  # 우리가 들릴 노드들이 다 기록
visited = [0] * (N + 1)

DFS(N)
print(len(path) - 1)