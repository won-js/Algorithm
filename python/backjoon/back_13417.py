import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = []
strings = []

for _ in range(n):
    nums.append(int(input().rstrip()))
    strings.append(list(input().rstrip().split(" ")))

for i in range(n):
    now = ord(strings[i][0])
    answer = strings[i][0]
    for j in range(1, nums[i]):
        char = strings[i][j]
        if now >= ord(char):
            now = ord(char)
            answer = char + answer
        else:
            answer = answer + char
    print(answer)
