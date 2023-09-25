N = int(input())
nums = list(map(int, input().split()))
max_sum = nums[0]
mid = 0
for i in range(N):
    mid += nums[i]
    if mid <0 and max_sum >=0:
        mid = 0
    elif mid <0 and max_sum <0:
        mid = max(max_sum, mid, nums[i])
    if mid > max_sum:
        max_sum = mid
print(max_sum)