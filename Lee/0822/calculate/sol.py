import sys

sys.stdin = open('input (3).txt')


def postorder(node):
    if node != 0:
        postorder(left[node])
        postorder(right[node])
        stack.append(word[node])


for test in range(10):
    N = int(input())
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    word = [''] * (N + 1)
    stack = []
    for i in range(N):
        Li = list(input().split())
        if len(Li) == 4:
            a, b, c, d = Li
            left[int(a)] = int(c)
            right[int(a)] = int(d)
            word[int(a)] = b
        else:
            a, b = Li
            word[int(a)] = int(b)
    # print(word)
    # print(left)
    # print(right)
    postorder(1)
    # print(stack)

    nw_stack = []
    for i in stack:
        if type(i) == int:
            nw_stack.append(i)
        else:
            a = nw_stack.pop()
            b = nw_stack.pop()
            if i == '+':
                nw_stack.append(a + b)
            elif i == '-':
                nw_stack.append(b - a)
            elif i == '*':
                nw_stack.append(a * b)
            else:
                nw_stack.append(b / a)

    print(f'#{test+1}', int(nw_stack[0]))
