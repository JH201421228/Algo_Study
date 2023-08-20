import sys
sys.stdin = open('input (13).txt')

Testcase = int(input())
for test in range(Testcase):
    # N은 판의 크기, M은 글자크기
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    final = 0
    for i in range(N):
        mid = 0
        for j in range(N):
            if Board[i][j] == 1:
                mid += 1
            else:
                if mid == M:
                    final += 1
                mid = 0
        if mid == M:
            final += 1

    for i in range(N):
        mid = 0
        for j in range(N):
            if Board[j][i] == 1:
                mid += 1
            else:
                if mid == M:
                    final += 1
                mid = 0
        if mid == M:
            final += 1

    print(f'#{test+1}', final)