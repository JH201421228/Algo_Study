N = int(input())
nums = list(map(int, input().split()))

max_acc = max(nums)
acc = nums[:]
for i in range(N):
    compare = []
    for j in range(i):
        if nums[i] > nums[j]:
            compare.append(acc[j])
        if compare:
            acc[i] = max(compare) + nums[i]
            if acc[i] > max_acc:
                max_acc = acc[i]

print(max_acc)