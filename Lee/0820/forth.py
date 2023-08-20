import sys
sys.stdin = open('sample_input (4).txt')

Testcase = int(input())
numbers = list(input().split())
stack = []
for i in numbers:
    if i in '+-*/':
