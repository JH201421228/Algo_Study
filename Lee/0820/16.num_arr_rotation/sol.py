import sys
sys.stdin = open('input (12).txt')

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    Board = [list(input().split()) for _ in range(N)]
    String = ['']*N
    for i in range(N):
        for j in range(N):
            String[i] += Board[N-1-j][i]
        String[i] += ' '
        for j in range(N):
            String[i] += Board[N-1-i][N-1-j]
        String[i] += ' '
        for j in range(N):
            String[i] += Board[j][N-1-i]
    print(f'#{test+1}')
    for i in String:
        print(i)