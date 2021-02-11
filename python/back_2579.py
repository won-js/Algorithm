n = int(input())

steps = []
for _ in range(n):
    steps.append(int(input()))

dp = [0] * (n+1)

dp[1] = 10
dp[2] = 20

for i in range(3,n):
    dp[i] = max(dp[i-1], dp[i-2]+steps[i])

print(max(dp[n],dp[n-1]+steps[-1]))