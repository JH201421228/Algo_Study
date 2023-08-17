Board = [list(input()) for _ in range(5)]
List = []
for j in range(15):
    for i in range(5):
        try:
            List.append(Board[i][j])

        except IndexError:
            continue
str = ''
for k in List:
    str += k

print(str)