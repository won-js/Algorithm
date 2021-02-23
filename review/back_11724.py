import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(" "))

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().rstrip().split(" "))
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)


def bfs(v):
    visited[v] = True
    q = deque([v])
    while q:
        now = q.popleft()
        for node in graph[now]:
            if not visited[node]:
                visited[node] = True
                q.append(node)

    return 1


count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += bfs(i)
print(count)
