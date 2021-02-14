import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(" "))
result = 0

miles = []
for _ in range(n):
    a, b = map(int, input().rstrip().split(" "))
    array = list(map(int, input().rstrip().split(" ")))

    if m < 1:
        continue
    if a < b:
        m -= 1
        result += 1
    else:
        array.sort()
        miles.append(array[a - b])

miles.sort()

for mile in miles:
    if m >= mile:
        result += 1
        m -= mile
    else:
        break

print(result)