import sys

input = sys.stdin.readline

n = int(input().rstrip())

dp = [0] * 31

dp[2] = 3
for i in range(4, n + 1, 2):

    dp[i] = 3 * dp[i - 2]
    for j in range(4, i, 2):
        dp[i] += 2 * dp[i - j]
    dp[i] += 2

print(dp[n])