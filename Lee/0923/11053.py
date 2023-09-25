N = int(input())
nums = list(map(int, input().split()))
acc = [1]*(N)
# print(nums)
# print(acc)

for i in range(N):
    mid = []
    for j in range(i):
        if nums[j]<nums[i]:
            mid.append(acc[j]+1)
    if mid:
        acc[i] = max(mid)
print(max(acc))