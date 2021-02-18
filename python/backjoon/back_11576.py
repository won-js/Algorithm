import sys

input = sys.stdin.readline

a, b = map(int, input().rstrip().split(" "))
m = int(input().rstrip())
arr = list(map(int, input().rstrip().split(" ")))

ten = 0
count = 0
for i in range(len(arr) - 1, -1, -1):
    ten += arr[i] * (a ** count)
    count += 1

answer = ""
while ten != 0:
    answer = str(ten % b) + " " + answer
    ten = ten // b
print(answer)