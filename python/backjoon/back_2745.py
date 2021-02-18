import sys

input = sys.stdin.readline

n, b = input().rstrip().split(" ")

answer = 0

arr = []
for i in range(len(n)):
    now = ord(n[i])
    if now >= 65 and now <= 90:
        arr.append(ord(n[i]) - 55)
    else:
        arr.append(int(n[i]))

count = 0
for i in range(len(arr) - 1, -1, -1):
    answer += arr[i] * (int(b) ** count)
    count += 1
print(answer)
