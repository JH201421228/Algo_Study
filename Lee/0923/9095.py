# 1을 만드는 방법은 하나  1  1
# 2를 만드는 방법은 둘   11 2   2
# 3을 만드는 방법은     111 21 12 3    4
# 4를 만드는 방법 1111 121 211 112 13 31 4    7
# 5를 만드는 방법 11111(1가지) 1112(4가지) 122(3가지) 113(3가지) 23(2가지)

def pl(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return pl(n - 1) + pl(n - 2) + pl(n - 3)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    print(pl(n))
