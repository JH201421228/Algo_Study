import sys
sys.stdin = open('sample_input (4).txt')

Testcase = int(input())
for test in range(Testcase):
    N, M, G = map(int, input().split())
    score = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        score[a] = b
    print(score)
    # N-M부터 앞까지 쭉 비어있음
    for i in range(N-M):
        try:
            score[N-M-i] = score[2*(N-M-i)] + score[2*(N-M-i)+1]
        except IndexError:
            score[N-M-i] = score[2*(N-M-i)]
        print(score)
    # print(score)
    print(f'#{test+1}', score[G])