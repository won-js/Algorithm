import sys

input = sys.stdin.readline

n, b = map(int, input().rstrip().split(" "))

arr = []
while n != 0:
    arr.append(n % b)
    n = n // b

for i in range(len(arr) - 1, -1, -1):
    if arr[i] >= 10:
        print(chr(arr[i] + 55), end="")
    else:
        print(arr[i], end="")
