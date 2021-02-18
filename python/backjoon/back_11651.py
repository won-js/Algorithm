import sys

input = sys.stdin.readline

n = int(input().rstrip())
array = []

for _ in range(n):
    array.append(list(map(int, input().rstrip().split(" "))))

array = sorted(array, key=lambda x: x[0])
array = sorted(array, key=lambda x: x[1])

for i in range(len(array)):
    print(str(array[i][0]), str(array[i][1]))
