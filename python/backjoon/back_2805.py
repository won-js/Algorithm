import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(" "))

trees = list(map(int, input().rstrip().split(" ")))

start = 1
end = max(trees)

answer = 0
while start <= end:
    count = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree > mid:
            count += tree - mid
    if count >= m:
        start = mid + 1
        answer = max(answer, mid)
    else:
        end = mid - 1

print(answer)