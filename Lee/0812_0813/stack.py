import sys
sys.stdin = open('b.txt')

Testcase = int(input())
for test in range(Testcase):
    obj = input()
    stack = []
    c = 0
    for i in obj:
        if i == '(' or i == '{' or  i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                c = -1
                break
        elif i == '}':
            if len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            else:
                c = -1
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                c = -1
                break
    if stack or c == -1:
        print(0)
    else:
        print(1)