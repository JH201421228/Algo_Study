A, B = input().split()
B = int(B)
N = len(A)
summ = 0
# 55를 빼줘야 함(65부터 90까지라면)
# 48을 빼줘야 함(48부터 57까지라면)
for i in range(N):
    if 65 <= ord(A[i]) <= 90:
        summ += B**(N-i-1) * (ord(A[i]) - 55)
    else:
        summ += B**(N-i-1) * (ord(A[i]) - 48)
print(summ)