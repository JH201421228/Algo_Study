import sys
sys.stdin = open('input (1).txt')

for _ in range(10):
    test = int(input())
    Board = [list(map(int, input().split())) for _ in range(100)]
    final = 0
    for i in range(100):
        if sum(Board[i])>= final:
            final = sum(Board[i])
    for i in range(100):
        mid = 0
        for j in range(100):
            mid += Board[j][i]
        if mid >= final:
            final = mid

    ne = me = 0
    for i in range(100):
        ne += Board[i][i]
        me += Board[99-i][i]
    print(f'#{test}', max(ne, me, final))