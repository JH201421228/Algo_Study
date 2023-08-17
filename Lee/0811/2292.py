N = int(input())
if N == 1:
    print(1)
else:
    k = 2
    Li = []
    while 1+3*(k-1)*(k-2) >= N or N > 1+3*k*(k-1):
        Li.append(k)
        k += 1
    if Li:
        print(Li[-1]+1)
    else:
        print(2)