import sys
sys.stdin = open('input.txt')

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    Board = [list(map(int, input())) for _ in range(N)]
    final = 0
    for i in range(N//2 + 1):
        for j in range(N//2-i, N//2+i+1):
            final += Board[i][j]
    for i in range(N//2+1, N):
        for j in range(N//2-(N-1-i), N//2+(N-1-i)+1):
            final += Board[i][j]
    print(f'#{test+1}', final)