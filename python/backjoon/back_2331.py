import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, p):
    q = deque([start])
    visited[start] += 1
    while q:
        now = str(q.popleft())
        answer = 0
        for i in range(len(now)):
            answer += int(now[i]) ** p
        visited[answer] += 1
        if visited[answer] == 3:
            return
        q.append(answer)
    return


visited = [0] * (4 * (9 ** 5) + 1)
a, p = map(int, input().rstrip().split(" "))
bfs(a, p)
count = 0
for i in range(1, len(visited)):
    if visited[i] == 1:
        count += 1
print(count)
