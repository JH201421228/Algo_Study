n = int(input())
lst = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: x[0])

h = 0
idx = 0
for i in range(n):
    if h < lst[i][1]:
        h = lst[i][1]
        idx = i

height = lst[0][1]
cnt = 0
for i in range(idx):
    if height < lst[i+1][1]:
        cnt += height * (lst[i+1][0] - lst[i][0])
        height = lst[i+1][1]
    else:
        cnt += height * (lst[i+1][0] - lst[i][0])

height = lst[-1][1]
for i in range(n - 1, idx, -1):
    if height < lst[i-1][1]:
        cnt += height * (lst[i][0] - lst[i - 1][0])
        height = lst[i-1][1]
    else:
        cnt += height * (lst[i][0] - lst[i-1][0])

cnt += h

print(cnt)