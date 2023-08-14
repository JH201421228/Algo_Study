import sys
sys.stdin = open('input (8).txt')

Testcase = 10
for test in range(Testcase):
    N = int(input())
    String = input()
    stack = []
    result = ''
    for char in String:
        if char == '+':
            while stack:
                result += stack.pop()
            stack.append(char)
        elif char == '*':
            if stack and stack[-1] == '*':
                result += char
            else:
                stack.append(char)

        else:
            result += char

    while stack:
        result += stack.pop()


    Stac = []
    for chr in result:
        Stac.append(chr)
        if chr == '+':
            Stac.pop()
            Stac.append(int(Stac.pop()) + int(Stac.pop()))
        elif chr == '*':
            Stac.pop()
            Stac.append(int(Stac.pop()) * int(Stac.pop()))

    print(f'#{test+1}', Stac[0])