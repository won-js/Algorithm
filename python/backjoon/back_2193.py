n = int(input())

if n == 1:
    print(1)
else:
    dp = [[0, 0] for _ in range(n + 1)]
    dp[1][1] = 1
    dp[2][0] = 1

    for i in range(3, n + 1):
        dp[i][0] = dp[i - 1][1] + dp[i - 1][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

    print(sum(dp[n]))