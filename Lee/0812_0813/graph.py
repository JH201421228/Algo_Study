import sys
sys.stdin = open('sample_input.txt')

def DFS(S, G):
    stack = [S]
    visited = [0]*(V+1)
    while stack:
        now = stack.pop()
        if visited[now] == 0:
            visited[now] == 1
            for next in range(1, V+1):
                if Board[now][next] == 1 and visited[next] == 0:
                    if next == G:
                        return 1
                    else:
                        stack.append(next)
    return 0

Testcase = int(input())
for test in range(Testcase):
    # 점과 선의 개수 파악
    V, E = map(int, input().split())
    # 인접행렬 정보 기입
    Board = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        Board[i][j] = 1
    # 시작점과 도착점 기입
    S, G = map(int, input().split())

    # S에서 G로 갈 수 있으면 1 못 가면 0을 반환하는 함수 만들자.
    print(f'#{test+1}', DFS(S, G))