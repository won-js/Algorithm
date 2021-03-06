import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(" "))

array = [int(input().rstrip()) for _ in range(n)]

start = 1
end = max(array)

answer = 0
while start <= end:
    count = 0
    mid = (start + end) // 2
    for line in array:
        count += line // mid
    if count >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)