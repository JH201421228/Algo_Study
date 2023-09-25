N = int(input())
dp = [50001 for i in range(N+1)]
dp[0] = 0
for i in range(1, N+1):
    for j in range(1, i+1):
        val = j*j
        if val > i:
            break
        dp[i] = min(dp[i], dp[i - val] + 1)
print(dp[N])