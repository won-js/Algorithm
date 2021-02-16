n = int(input())

INF = int(1e9)

dp = [INF] * 100001
dp[0] = 0

for i in range(1, n + 1):
    j = 1
    while j ** 2 <= i:
        dp[i] = min(dp[i], dp[i - j ** 2] + 1)
        j += 1
print(dp[n])