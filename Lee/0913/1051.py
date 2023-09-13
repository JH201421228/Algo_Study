import sys
sys.stdin = open('1051.txt')

N, M = map(int, input().split())
Board = [list(map(int, input())) for _ in range(N)]
final = 1

for i in range(N-1):
    for j in range(M-1):
        start = Board[i][j]
        width = set()
        height = set()
        for k in range(i+1, N):
            if Board[k][j] == start:
                width.add(k-i+1)
        for l in range(j+1, M):
            if Board[i][l] == start:
                height.add(l-j+1)
        if width&height:
            a = max(width & height)
            if Board[i+a-1][j+a-1] == Board[i][j]:
                if final <= a:
                    final = a
print(final**2)