from collections import deque
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

t = int(input().rstrip())


def dfs(start):
    visited[start] = True
    global cycle
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
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    color = [False] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().rstrip().split(" "))
        graph[a].append(b)
        graph[b].append(a)

    cycle = False

    for i in range(1, v + 1):
        if not visited[i] and not cycle:
            dfs(i)

    if cycle:
        print("NO")
    else:
        print("YES")
