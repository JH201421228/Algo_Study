import sys
input = sys.stdin.readline

K, N = map(int, input().split())
rans = [int(input()) for _ in range(K)]
# print(rans)

start = 1
end = max(rans)
final = 0

while start <= end:
    mid = (start+end)//2
    summ = 0
    for ran in rans:
        summ += ran//mid

    if summ >= N:
        final = mid
        start = mid + 1
    else:
        end = mid - 1
print(final)