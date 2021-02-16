import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split(" "))

dp = [[0] * 201 for _ in range(201)]

for i in range(1, k + 1):
    dp[i][0] = 1

for i in range(1, k + 1):
    for j in range(1, n + 1):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000

print(dp[k][n])
