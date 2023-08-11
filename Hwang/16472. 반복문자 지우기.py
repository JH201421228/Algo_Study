T = int(input())

for t in range(1, T+1):
    N = list(input())

    stack = []

    for i in N:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()

    result = len(stack)

    print(f'#{t} {result}')
