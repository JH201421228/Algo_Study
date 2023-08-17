Board = [list(map(int, input().split())) for _ in range(9)]
maximum = 0
a = b = 0
for i in range(9):
    for j in range(9):
        if Board[i][j]>=maximum:
            maximum = Board[i][j]
            a = i
            b = j
print(maximum)
print(a+1, b+1)