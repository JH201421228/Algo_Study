import sys
input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

maxi = max(trees)
start = 0
end = maxi

while start <= end:
    sum = 0
    mid = (start+end)//2
    for tree in trees:
        if tree <= mid:
            pass
        else:
            sum += tree-mid

        if sum >= M:
            start = mid+1
    if sum < M:
        end = mid-1
print(end)