from itertools import product

N, n = input().split()
Number = set(input().split())
List = []

for j in range(len(N)):
    for i in product(Number, repeat = len(N)-j):
        str = ''
        for k in i:
            str += k
        if int(N) >= int(str):
            List.append(int(str))
        else:
            continue
print(max(List))