import sys
sys.stdin = open('youngjun.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    price = ['UNKNOWN']*(N+1)
    print(f'#{tc}', end=' ')
    for i in range(M):
        a, *b = list(input().split())
        # !를 만나면
        if a == '!':
            c, d, e = map(int,b)
            if price[c] == 'UNKNOWN' and price[d] == 'UNKNOWN':
                price[c] = 0
                price[d] = e

            elif price[c] == 'UNKNOWN':
                price[c] = price[d] - e
            elif price[d] == 'UNKNOWN':
                price[d] = price[c] + e
        # ? 를 만나면
        else:
            c, d = map(int, b)
            if price[c] != 'UNKNOWN' and price[d] != 'UNKNOWN':
                print(price[d] - price[c], end=' ')
            else:
                print('UNKNOWN', end=' ')
    print()