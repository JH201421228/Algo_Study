import sys
sys.stdin = open('1932.txt')

N = int(input())
Board = [list(map(int, input().split())) for _ in range(N)]

for i in range(1 << N-1):
    l = m = 0
    mid = Board[l][m]
    for j in range(N-1):
        if i & (1 << j):
            l += 1
            m += 1
            mid += Board[l][m]
        else:
            l += 1
            mid += Board[l][m]
    if mid >= maximum:
        maximum = mid


print(maximum)