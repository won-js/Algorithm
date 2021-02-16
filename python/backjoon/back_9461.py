import sys

input = sys.stdin.readline

t = int(input().rstrip())

testcase = []

for _ in range(t):
    testcase.append(int(input().rstrip()))

dp = [1] * 101
dp[4] = 2
dp[5] = 2
for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

for case in testcase:
    print(dp[case])