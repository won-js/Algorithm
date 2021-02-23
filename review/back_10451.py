import sys
from collections import deque

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

# def dfs(start):
#     visited[start] = True
#     for node in graph[start]:
#         if not visited[node]:
#             dfs(node)

#     return 1


for _ in range(t):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split(" ")))
    graph = [[] for _ in range(n+1)]

    for i in range(len(arr)):
        graph[i+1].append(arr[i])
        graph[arr[i]].append(i+1)

    visited = [False] * (n+1)

    answer = 0
    for i in range(1, n+1):
        if not visited[i]:
            answer += bfs(i)
    print(answer)
