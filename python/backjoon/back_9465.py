import sys

input = sys.stdin.readline

n = int(input().rstrip())
testcase = [[] for _ in range(n)]

for i in range(n):
    a = int(input().rstrip())
    testcase[i].append(list(map(int, input().rstrip().split(" "))))
    testcase[i].append(list(map(int, input().rstrip().split(" "))))

for i in range(n):
    up = testcase[i][0]
    down = testcase[i][1]

    length = len(up)

    dp = [[0] * (length + 1) for _ in range(2)]
    dp[0][1] = up[0]
    dp[1][1] = down[0]
    if length == 1:
        print(max(up[0], down[0]))
    dp[0][2] = dp[1][1] + up[1]
    dp[1][2] = dp[0][1] + down[1]
    if length == 2:
        print(max(dp[0][2], dp[1][2]))
    for j in range(3, length + 1):
        dp[0][j] = max(dp[0][j - 2], dp[1][j - 2], dp[1][j - 1]) + up[j - 1]
        dp[1][j] = max(dp[0][j - 2], dp[1][j - 2], dp[0][j - 1]) + down[j - 1]

    print(max(dp[0][-1], dp[1][-1]))