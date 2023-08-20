import sys
sys.stdin = open('sample_input (2).txt')

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    Red = set()
    Blue = set()
    for _ in range(N):
        x1, y1, x2, y2, c = map(int, input().split())
        if c == 1:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    Red.add((i, j))
        else:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    Blue.add((i, j))
    Purple = Red & Blue
    print(f'#{test+1}', len(Purple))