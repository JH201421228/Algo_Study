n, t, k = map(int, input().split())
if n == 0:
    print(1)
else:
    rank = list(map(int, input().split()))
    ans = 0

    rank.append(t)
    rank.sort(reverse=True)
    idx = rank.index(t) + 1

    if idx > k:
        print(-1)
    else:
        if n == k and t == rank[-1]:
            print(-1)
        else:
            print(idx)



