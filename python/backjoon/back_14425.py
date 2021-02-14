import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(" "))

count = 0

S = []
for _ in range(n):
    S.append(input().rstrip())

check = []
for _ in range(m):
    check.append(input().rstrip())

for string in check:
    if string in S:
        count += 1

print(count)