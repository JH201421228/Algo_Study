import sys
sys.stdin = open('c.txt')

Testcase = int(input())
for test in range(Testcase):
    string = input()
    stack = []
    c = 0
    for i in string:
        if i == '(':
            stack.append(i)

        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                c = -1
                break
    if c == -1 or stack:
        print(f'#{test+1} 괄호가 잘못되었습니다.')
    else:
        print(f'#{test+1} 옳게 된 괄호입니다.')
