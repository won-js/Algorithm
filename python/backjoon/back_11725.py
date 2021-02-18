import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().rstrip().split(" "))
    graph[a].append(b)
    graph[b].append(a)
if n == 2:
    print(1)
else:
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)

    q = deque()
    for num in graph[1]:
        q.append(num)
        parent[num] = 1
    visited[1] = True
    while q:
        now = q.popleft()
        visited[now] = True
        for node in graph[now]:
            if not visited[node]:
                parent[node] = now
                q.append(node)

    for i in range(2, n + 1):
        print(parent[i])