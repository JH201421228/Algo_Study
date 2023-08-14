N, K = int(input())
numbers = list(input().split())

str = ''
while len(str) <= K:
    str = ''
    for i in range(K):
        for j in range(K):
