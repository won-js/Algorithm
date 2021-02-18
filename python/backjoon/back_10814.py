import sys

input = sys.stdin.readline

n = int(input().rstrip())

arr = []
for _ in range(n):
    arr.append(list(input().rstrip().split(" ")))

arr = sorted(arr, key=lambda x: int(x[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])
