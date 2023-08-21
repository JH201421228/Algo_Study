import sys
sys.stdin = open('b.txt')


N = int(input())
stack = []
complete = 0
middle = 0

for i in range(N):
    a, b = map(int, input().split())
    stack.append(range(a, b+1))