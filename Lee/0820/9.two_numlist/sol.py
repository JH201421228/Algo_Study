import sys
sys.stdin = open('input (2).txt')

Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())
    AN = list(map(int, input().split()))
    BM = list(map(int, input().split()))
    maximum = 0
    for k in range(min(N, M)):
        maximum += AN[k] * BM[k]

    for i in range(abs(N-M)):
        mid = 0
        if N <= M:
            for j in range(N):
                mid += AN[j] * BM[j]
            BM.pop(0)
            if mid >= maximum:
                maximum = mid


        else:
            for j in range(M):
                mid += AN[j] * BM[j]
            AN.pop(0)
            if mid >= maximum:
                maximum = mid

    last = 0
    for k in range(min(N, M)):
        last += AN[k] * BM[k]

    print(f'#{test+1}', max(maximum, last))