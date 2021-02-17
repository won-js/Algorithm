import sys

input = sys.stdin.readline

n = int(input().rstrip())

arr = []

for _ in range(n):
    arr.append(list(input().rstrip().split(" ")))

arr = sorted(arr, key=lambda x: x[0])
arr = sorted(arr, key=lambda x: int(x[3]), reverse=True)
arr = sorted(arr, key=lambda x: int(x[2]))
arr = sorted(arr, key=lambda x: int(x[1]), reverse=True)

for stu in arr:
    print(stu[0])
