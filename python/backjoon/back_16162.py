import sys

input = sys.stdin.readline

n, a, d = map(int, input().rstrip().split(" "))
array = list(map(int, input().rstrip().split(" ")))

result = 0
idx = 0

for num in array:
    if num == a + idx * d:
        result += 1
        idx += 1

print(result)