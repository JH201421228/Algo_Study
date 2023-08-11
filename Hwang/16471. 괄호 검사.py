T = int(input())

for t in range(1, T+1):
    string = list(input())

    find_str = ['(', ')', '{', '}']
    stack = []

    # print(string)

    for i in string:
        if i in find_str:
            if len(stack) == 0 or i == '(' or i == '{':
                stack.append(i)
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()

    if len(stack) == 0:
        print(f'#{t}', 1)
    else:
        print(f'#{t}', 0)

--------------------


T = int(input())

for t in range(1, T+1):
    string = list(input())

    find_str = ['(', ')', '{', '}']
    stack = []

    # print(string)
    # print('{} {}'.format(1, 2)(}))
    for i in string:
        if i in find_str:
            if len(stack) == 0 or i == '(' or i == '{':
                stack.append(i)
            if i == ')':
                if stack[-1] == '(':
                    stack.pop()
                elif i == ')':
                    stack.append(i)
            if i == '}':
                if stack[-1] == '{':
                    stack.pop()
                elif i == '}':
                    stack.append(i)

    if len(stack) == 0:
        print(f'#{t}', 1)
    else:
        print(f'#{t}', 0)