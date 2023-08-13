# memoization
def factorial(n):
    global memo
    if n == 0:
        memo[0] = 1
        return memo[0]
    else:
        memo[n] = n*factorial(n-1)
        return memo[n]

N = 500
memo = [0] * (N+1)
print(factorial(N))