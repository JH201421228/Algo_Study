import sys
sys.stdin = open('say_col.txt')

T = int(input())
for tc in range(1, T+1):
    Board = [list(input()) for _ in range(5)]
    final = ''
    maximum = max([len(Board[i]) for i in range(5)])
    for i in range(5):
        while len(Board[i]) != maximum:
            Board[i].append(-1)
    for i in range(maximum):
        for j in range(5):
            if Board[j][i] != -1:
                final += Board[j][i]
    print(f'#{tc}', final)