from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().rstrip().split(" "))

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().rstrip().split(" "))
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()


def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for node in graph[v]:
        if not visited[node]:
            dfs(node)


def bfs(v):
    visited[v] = True
    q = deque([v])
    while q:
        now = q.popleft()
        print(now, end=" ")
        for node in graph[now]:
            if not visited[node]:
                visited[node] = True
                q.append(node)


visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
