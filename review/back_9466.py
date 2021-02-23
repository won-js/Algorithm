import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(start):
    global answer
    visited[start] = True
    loop.append(start)
    next_value = graph[start]

    if visited[next_value]:
        if next_value in loop:
            answer += len(loop[loop.index(next_value):])
        return
    else:
        dfs(next_value)


t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    graph = [0] + list(map(int, input().rstrip().split(" ")))
    answer = 0
    visited = [False] * (n+1)
    for i in range(1, len(graph)):
        if not visited[i]:
            loop = []
            dfs(i)
    print(n - answer)
