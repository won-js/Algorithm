import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

t = int(input().rstrip())


def dfs(start):
    global cycle
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            color[node] = not color[start]
            dfs(node)
        elif color[node] == color[start]:
            cycle = True
            return
    return

for _ in range(t):
    v, e = map(int, input().rstrip().split(" "))
    graph = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    color = [False] * (v+1)
    for _ in range(e):
        a, b = map(int, input().rstrip().split(" "))
        graph[a].append(b)
        graph[b].append(a)
    cycle = False
    for i in range(1, v+1):
        if not visited[True] and not cycle:
            dfs(i)

    if cycle:
        print("NO")
    else:
        print("YES")
