from collections import deque
import sys
sys.stdin = open('11403.txt')
input = sys.stdin.readline

def BFS(n):
    visited = [0]*N
    Q = deque([n])
    while Q:
        now = Q.popleft()
        for next in range(N):
            if Board[now][next] == 1 and visited[next] == 0:
                Q.append(next)
                visited[next] = 1
    return visited

N = int(input())
Board = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    print(*BFS(i))