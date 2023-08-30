N = int(input())
i = 0
if N == 4 or N == 7:
    print(-1)
else:
    a = N // 5
    if (N % 5) % 3 == 0:
        b = (N % 5) // 3
    else:
        while ((N % 5) + 5 * i) % 3 != 0:
            i += 1
        b = ((N % 5) + 5 * i) // 3
    print(a - i + b)
