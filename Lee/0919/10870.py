def fibo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        Memo[n] = 1
        return Memo[n]
    else:
        Memo[n] = fibo(n-1)+fibo(n-2)
        return Memo[n]

Memo = [0]* 21
print(fibo(int(input())))