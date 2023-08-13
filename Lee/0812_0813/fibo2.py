# memoization
N = 10
memo = [0] * (N+1)

def fibo(n):
    if n<=1:
        memo[n] = n
        return memo[n]
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]

print(fibo(10))