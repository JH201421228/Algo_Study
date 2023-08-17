import sys
sys.stdin = open('b.txt')

N = int(input())
numbers = list(map(int, input().split()))
up = 1
dwn = 1
maxi = 1
i = 0
while i != N-1:
    if numbers[i] == numbers[i+1]:
        up += 1
        dwn += 1

    elif numbers[i] < numbers[i+1]:
        up += 1
        if maxi <= dwn:
            maxi = dwn
        dwn = 1
    else:
        if maxi <= up:
            maxi = up
        up = 1
        dwn += 1
    i += 1

print(max(maxi, up, dwn))