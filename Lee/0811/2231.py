N = int(input())
final = []
for M in range(1, N):
    List = [int(i) for i in str(M)]
    spl_sum = M
    for i in List:
        spl_sum += i

    if spl_sum == N:
        final.append(M)
if final:
    print(min(final))
else:
    print(0)