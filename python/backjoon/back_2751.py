import sys

input = sys.stdin.readline

n = int(input().rstrip())

array = []
for _ in range(n):
    array.append(int(input().rstrip()))

array.sort()

for num in array:
    print(num)