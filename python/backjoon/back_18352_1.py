from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().rstrip().split(" "))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split(" "))
    graph[a].append(b)

distance = [-1] * (n + 1)

distance[x] = 0
q = deque()
q.append(x)

while q:
    now = q.popleft()
    for node in graph[now]:
        if distance[node] == -1:
            distance[node] = distance[now] + 1
            q.append(node)

answer = False
for i in range(1, len(distance)):
    if distance[i] == k:
        print(i)
        answer = True

if not answer:
    print(-1)