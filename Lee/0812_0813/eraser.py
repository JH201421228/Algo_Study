import sys
sys.stdin = open('d.txt')

Testcase = int(input())
for test in range(Testcase):
    String = input()
    stack = []
    for i in String:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print(f'#{test+1}', len(stack))