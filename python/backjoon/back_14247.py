import sys

input = sys.stdin.readline

n = int(input().rstrip())

trees = list(map(int, input().rstrip().split(" ")))
growth = list(map(int, input().rstrip().split(" ")))

result = 0
leng = len(trees)

array = list(zip(trees,growth))

array = sorted(array, key=lambda x: x[1])

for i in range(n):
    result += array[i][1] * i + array[i][0]

print(result)