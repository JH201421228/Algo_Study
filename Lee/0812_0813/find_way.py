import sys
sys.stdin = open('input (5).txt')

def DFS():
    stack = [0]
    visited = [0]*100
    while stack:
        now = stack.pop(0)
        visited[now] = 1
        for i in range(100):
            if Board[now][i] == 1 and visited[i] == 0:
                if i == 99:
                    return 1
                else:
                    stack.append(i)
    return 0

while 1:
    try:
        test, E = map(int, input().split())
        Li = list(map(int, input().split()))
        Board = [[0]*100 for _ in range(100)]
        for i in range(E):
            Board[Li[2*i]][Li[2*i+1]] = 1

        print(f'#{test}', DFS())

    except EOFError:
        break