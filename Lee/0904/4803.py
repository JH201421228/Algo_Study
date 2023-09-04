from collections import deque
import sys
sys.stdin = open('4803.txt')

def is_cycle(node):
    visited = [0]*(n+1)
    Q = deque([node])
    while Q:
        now = Q.popleft()
        if visited[now] == 0:
            visited[now] = 1
        else:
            return True
        for next in Board[now]:
            if visited[next] == 0:
                Q.append(next)
    return False

tc = 0
while 1:
    tc += 1
    tree = 0
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    else:
        Board = [[] for _ in range(n+1)]
        for _ in range(m):
            a, b = map(int, input().split())
            Board[a].append(b)
            Board[b].append(a)
    print(Board)
    for i in range(1, n+1):
        print(is_cycle(i))


    if tree > 1:
        print(f'Case {tc}: A forest of {tree} trees.')
    elif tree == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: No trees.')