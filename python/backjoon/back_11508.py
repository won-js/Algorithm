import sys

input = sys.stdin.readline

array = []
n = int(input().rstrip())

for _ in range(n):
    array.append(int(input().rstrip()))

array.sort(reverse=True)

idx = 0
result = 0
for num in array:
    idx += 1
    if idx % 3 == 0:
        continue
    result += num

print(result)