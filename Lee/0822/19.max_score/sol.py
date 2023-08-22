import sys
sys.stdin = open('sample_input.txt')

Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())
    score = list(map(int, input().split()))
    S = 0
    score.sort()
    for i in range(M):
        S += score.pop()
    print(f'#{test+1}', S)