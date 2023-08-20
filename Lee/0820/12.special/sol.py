import sys
sys.stdin = open('sample_input (2).txt')

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    numbers = list(map(int, input().split()))
    final = []
    numbers.sort()
    while numbers:
        final.append(numbers.pop())
        if numbers:
            final.append(numbers.pop(0))
        else:
            break
    final = final[:10]
    print(f'#{test+1}', *final)