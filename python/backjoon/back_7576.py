from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(N, M, graph):
    day = -1
    while q:
        day += 1
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx < N) and (0 <= ny < M) and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
    for g in graph:
        if 0 in g:
            return -1
    return day


m, n = map(int, input().rstrip().split(" "))
graph, q = [], deque()

for i in range(n):
    row = list(map(int, input().rstrip().split(" ")))
    graph.append(row)
    for j in range(len(row)):
        if row[j] == 1:
            q.append((i, j))

print(bfs(n, m, graph))
