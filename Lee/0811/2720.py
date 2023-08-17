Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    # 쿼터(25) / 다임(10) / 니켈(5) / 페니(1)
    Q = N//25
    N = N - Q * 25
    D = N//10
    N = N - D * 10
    Ni = N//5
    N = N - Ni * 5
    P = N
    print(Q, D, Ni, P)