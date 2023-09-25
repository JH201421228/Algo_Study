N = int(input())
memo = list(range(N+1))
if N <= 3:
    pass
else:
    n=3
    while n != N+1:
        memo[n] = memo[n-1]+memo[n-2]
        n+=1
print(memo[N]%10007)