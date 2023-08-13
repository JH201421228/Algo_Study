Testcase = int(input())
for test in range(Testcase):
    String = input()
    stack = []
    checking = ''
    for i in String:
        if i == '(' or i =='{':
            stack.append(i)

        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                checking = 'X'

        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                checking = 'X'
    if stack or checking == 'X':
        print(f'#{test+1}', 0)
    else:
        print(f'#{test+1}', 1)