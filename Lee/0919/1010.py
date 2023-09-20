from math import comb

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if a > b:
        print(comb(a, b))
    else:
        print(comb(b, a))