import sys
sys.stdin = open('10815.txt')

N = int(input())
A = set((input().split()))
M = int(input())
num = list(map(int, input().split()))
for m in num:
    if str(m) in A:
        print(1, end=' ')

    else:
        print(0, end=' ')