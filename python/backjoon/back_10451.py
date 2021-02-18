from collections import deque
import sys

input = sys.stdin.readline

t = int(input().rstrip())

def bfs(start):
    visited[start] = True
    q = deque([start])
    while q:
        now = q.popleft()
        for node in graph[now]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
    return 1


for _ in range(t):
    n = int(input().rstrip())
    graph = [[] for _ in range(n + 1)]

    nodes = [0] + list(map(int, input().rstrip().split(" ")))
    for i in range(1, +n + 1):
        graph[i].append(nodes[i])
        graph[nodes[i]].append(i)

    visited = [False] * (n + 1)
    cycle = 0
    for i in range(1, n + 1):
        if not visited[i]:
            cycle += bfs(i)
    print(cycle)
