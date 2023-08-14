def to_postfix(expression):
    oper = {'+': 1, '*': 2}
    res = []
    stack = []

    for i in expression:
        if i.isdigit():
            res.append(i)
        elif i in oper:
            if stack and (oper[i] <= oper[stack[-1]]):
                res.append(stack.pop())
            stack.append(i)
    while stack:
        res += stack.pop()
    return res


for t in range(1, 11):
    n = int(input())
    eq = input()
    s = []

    lst = to_postfix(eq)
    for i in lst:
        if i.isdigit():
            s.append(int(i))
        elif i == '+':
            s.append(s.pop() + s.pop())
        elif i == '*':
            s.append(s.pop() * s.pop())

    print(f'#{t}', *s)


