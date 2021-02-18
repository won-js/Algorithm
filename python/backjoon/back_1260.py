from collections import deque
import sys

input = sys.stdin.readline

n, m, start = map(int, input().rstrip().split(" "))

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().rstrip().split(" "))
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

visited = [False] * (n + 1)


def dfs(start):
    print(start, end=" ")
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(node)
    return 0


def bfs(start):
    q = deque([start])
    while q:
        now = q.popleft()
        if not visited[now]:
            visited[now] = True
            print(now, end=" ")
            for node in graph[now]:
                q.append(node)
    return 0


dfs(start)
print()
visited = [False] * (n + 1)
bfs(start)