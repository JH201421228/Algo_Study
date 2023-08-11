def cnt(n):
    if n % 10 == 0:
        if n == 10:
            return 1
        elif n == 20:
            return 3
        else:
            return 2 * cnt(n - 20) + cnt(n - 10)


for tc in range(int(input())):
    n = int(input())
    num = cnt(n)
    print(f'#{tc+1} {num}')

