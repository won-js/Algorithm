import sys
import math

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    arr = list(map(int, input().rstrip().split(" ")))
    answer = 0
    for i in range(1, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            answer += math.gcd(arr[i], arr[j])
    print(answer)