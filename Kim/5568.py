n = int(input())
k = int(input())


def perm(lst, n):
    result = []
    if n > len(lst):
        return result

    if n == 1:
        for i in lst:
            result.append([i])

    elif n > 1:
        for i in range(len(lst)):
            ans = [i for i in lst]
            ans.remove(lst[i])
            for p in perm(ans, n-1):
                result.append([lst[i]] + p)

    return result


num_lst = []
for _ in range(n):
    num_lst.append(str(input()))

my_lst = perm(num_lst, k)

lst = []
for i in my_lst:
    lst.append(''.join(i))

print(len(set(lst)))
