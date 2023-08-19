n, k = map(int, input().split())
number = list(map(int, input().split()))
my_lst = []
s = []  # [157]


def dfs(lst):
    if len(s) == len(lst):  # len(lst) 3
        my_lst.append(''.join(map(str, s)))
        return

    for i in range(k):  #2
        s.append(number[i])
        dfs(lst)
        s.pop()

dfs(number)

ans = 0
for i in range(len(my_lst)):
    my_lst[i] = int(my_lst[i])
    if my_lst[i] > n:
        ans = my_lst[i-1]
        break
    elif my_lst[i] == n:
        ans = my_lst[i]
        break

print(ans)

# 657 3
# 1 5 7