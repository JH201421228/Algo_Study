n = int(input())
arr = list(map(int, input().split()))
l = int(input())

if sum(arr) <= l:
    print(max(arr))

else:
    ans = 0
    start, end = 0, l

    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for a in arr:
            if a > mid:
                temp += mid
            else:
                temp += a

        if temp <= l:
            start = mid + 1
        else:
            end = mid - 1
    print(end)