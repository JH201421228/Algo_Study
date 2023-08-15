# 분해합   216   198 + 1 + 9 + 8 = 216
N = int(input())
final = []
for M in range(1, N):
    List = [int(i) for i in str(M)] # [1, 9, 8]
    spl_sum = M # 198
    for i in List:
        spl_sum += i

    if spl_sum == N:
        final.append(M)
if final:
    print(min(final))
else:
    print(0)