from itertools import combinations
import sys
sys.stdin = open('carrot.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()      # 당근을 크기순으로 정렬
    min_v = 1000    # 포장별 최소 개수 차이
    for i in range(N-2):
        for j in range(i+1, N-1):
            if arr[i] != arr[i+1] and arr[j] != arr[j+1]:
                small = i+1     # 소 상자에 들어간 당근 개수
                mid = j-i       # 중 상자에 들어간 개수
                large = N-1-j   # 대 상자에 들어간 개수
                if small <= N//2 and mid <= N//2 and large <= N//2:
                    if min_v >(max(small, mid, large) - min(small, mid, large)):
                        min_v = max(small, mid, large) - min(small, mid, large)
    if min_v == 1000:
        print(f'#{tc}', -1)
    else:
        print(f'#{tc}', min_v)