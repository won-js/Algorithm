import sys

input = sys.stdin.readline

n = int(input().rstrip())

array = [0] + list(map(int, input().rstrip().split(" ")))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    now = array[i]
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))