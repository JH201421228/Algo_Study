def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)


print(fibo(10))
#
# 0 1 2 3 4 5 6 7  8  9  10
# 0 1 1 2 3 5 8 13 21 34 55