import sys

input = sys.stdin.readline

n = int(input().rstrip())

glass = [0]
for _ in range(n):
    glass.append(int(input().rstrip()))
if n >= 3:
    dp = [0] * (n + 1)
    dp[1] = glass[1]
    dp[2] = glass[2] + dp[1]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 3] + glass[i - 1], dp[i - 2]) + glass[i]
        dp[i] = max(dp[i], dp[i - 1])
    print(dp[-1])
else:
    if n == 1:
        print(glass[1])
    else:
        print(glass[1] + glass[2])
