from collections import deque
import sys

input = sys.stdin.readline
a, b = map(int, input().rstrip().split(" "))


def bfs(a, b):
    q = deque([a])
    count = 1
    while q:
        length = len(q)
        count += 1
        for _ in range(length):
            now = q.popleft()
            x, y = now * 2, int(str(now) + str(1))
            if x == b or y == b:
                return count
            if x < b:
                q.append(x)
            if y < b:
                q.append(y)
    return -1


print(bfs(a, b))
