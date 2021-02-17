import sys

input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    arr.append(int(input().rstrip()))

dic = {}

for num in arr:
    if dic.get(num):
        dic[num] = dic.get(num) + 1
    else:
        dic[num] = 1

max_count = 0
min_value = 0

for key, value in dic.items():
    if value > max_count:
        min_value = key
        max_count = value
    elif value == max_count and key < min_value:
        min_value = key

print(min_value)