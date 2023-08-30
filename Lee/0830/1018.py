import sys
sys.stdin = open('1018.txt')

A = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
B = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
Board1 = [A, B]*4
Board2 = [B, A]*4


# T = int(input())
# for tc in range(1, T+1):
N, M = map(int, input().split())
Board = [list(input()) for _ in range(N)]
final = []
for i in range(N - 7):
    for j in range(M - 7):
        cnt_1 = 0
        cnt_2 = 0
        for l in range(8):
            for m in range(8):
                if Board[i + l][j + m] != Board1[l][m]:
                    cnt_1 += 1
                if Board[i + l][j + m] != Board2[l][m]:
                    cnt_2 += 1
        final.append(min(cnt_1, cnt_2))
print(min(final))
