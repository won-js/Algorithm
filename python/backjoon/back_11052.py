import sys

input = sys.stdin.readline

n = int(input().rstrip())

cards = [0] + list(map(int, input().rstrip().split()))

dp = [0] * (n + 1)
dp[1] = cards[1]
if n == 1:
    print(cards[1])
else:
    dp[2] = max(2 * dp[1], cards[2])
    for i in range(3, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i - j] + cards[j])

    print(dp[n])