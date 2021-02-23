import sys

from collections import deque

input = sys.stdin.readline

a, p = map(int, input().rstrip().split(" "))

d = [0] * (4*(9**5)+1)


def bfs(start, p):
    q = deque([start])
    d[start] += 1
    while q:
        now = str(q.popleft())
        count = 0
        for i in list(now):
            count += int(i)**p
        d[count] += 1
        if d[count] == 3:
            return
        else:
            q.append(count)


bfs(a, p)
answer = 0
for i in range(len(d)):
    if d[i] == 1:
        answer += 1
print(answer)
