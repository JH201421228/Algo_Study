import sys
input = sys.stdin.readline

from collections import deque

for t in range(1, int(input()) + 1):
    func = list(input())
    n = int(input())
    temp = input()
    flag = True

    temp = temp[1:]
    arr = deque()
    num = ""

    for char in temp:
        if char.isdigit():
            num += char
        elif char == ',' and num:
            arr.append(int(num))
            num = ""
        elif char == ']' and num:
            arr.append(int(num))
            num = ""

    if func.count('D') > n:
        flag = False

    for i in func:
        if not arr and 'D' in func:
            flag = False
            break
    cnt = 0
    for i in func:
        if not flag:
            break

        if i == 'R':
            cnt += 1

        elif i == 'D':
            if cnt % 2 == 0:
                arr.popleft()
            elif cnt % 2 != 0:
                arr.pop()

    if cnt % 2 == 1:
        arr.reverse()

    if flag:
        print('[', ",".join(map(str, arr)), ']', sep='')
    else:
        print('error')

# input 배열 길이가 50만 이상이라 진짜로 reverse하면 시간 초과남
# 즉 배열을 돌리지 않고 돌린것과 같은 효과를 내야함.
# 물론 R이 홀수라면 한번은 돌려야...
# deque를 통해 앞뒤쪽으로 pop할수 있도록 해서 시간 절약하기