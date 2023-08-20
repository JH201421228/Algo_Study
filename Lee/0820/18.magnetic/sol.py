import sys
sys.stdin = open('input (14).txt')

for test in range(1, 11):
    N = int(input())
    Board = [list(input().split()) for _ in range(100)]
    final = 0
    # 1은 N극(천장이니 바닥으로 밀림) 2는 S극(바닥이니 천장으로 올림)
    for i in range(100):
        String = ''
        for j in range(100):
            if Board[j][i] != '0':
                String += Board[j][i]
        final += String.count('12')

    print(f'#{test}', final)