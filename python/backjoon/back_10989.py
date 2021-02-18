import sys

input = sys.stdin.readline

preset = [0] * 10001
n = int(input().rstrip())

for _ in range(n):
    preset[int(input().rstrip())] += 1

for i in range(10001):
    now = preset[i]
    if now == 0:
        continue
    for j in range(now):
        print(i)
