import sys
sys.stdin = open('2493.txt')

N = int(input())
L = list(map(int, input().split()))
final = [0]*N
check_list = [0]*N

for i in range(1, N):
    if L[i]<L[i-1]:
        final[i-1] = i-1
    else:
