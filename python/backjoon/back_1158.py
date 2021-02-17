from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split(" "))
print("<", end="")

q = deque(list(range(1, n + 1)))


count = 0
while q:
    count += 1
    if count == k:
        if len(q) == 1:
            print(q.popleft(), end=">")
        else:
            print(q.popleft(), end=", ")
        count = 0
        continue
    q.append(q.popleft())