import sys

input = sys.stdin.readline

n = int(input().rstrip())
array = list(map(int, input().rstrip().split(" ")))

dp = [1] * (n)
for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

dp_des = [1] * (n)
for i in range(n - 1, 0, -1):
    for j in range(n - 1, i, -1):
        if array[i] > array[j]:
            dp_des[i] = max(dp_des[i], dp_des[j] + 1)

answer = 0
for i in range(n):
    answer = max(answer, dp[i] + dp_des[i])
answer = max(answer, dp[-1])

print(answer-1)
