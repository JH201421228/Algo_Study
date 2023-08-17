import sys
sys.stdin = open('1932.txt')

def merge(arr1, arr2):
    arr2[0] += arr1[0]
    arr2[-1] += arr1[-1]
    for i in range(1, len(arr2)-1):
        arr2[i] += max(arr1[i-1], arr1[i])
    return arr2

N = int(input())
Board = [list(map(int, input().split())) for _ in range(N)]
for i in range(N-1):
    merge(Board[i], Board[i+1])
print(max(Board[N-1]))