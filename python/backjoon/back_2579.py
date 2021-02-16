import sys

input = sys.stdin.readline

n = int(input().rstrip())
steps = [0]

for _ in range(n):
    steps.append(int(input().rstrip()))

dp = [0] * (n + 1)
dp[1] = steps[1]
dp[2] = steps[1] + steps[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + steps[i - 1], dp[i - 2]) + steps[i]

print(dp[n])