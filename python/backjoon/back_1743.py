import sys
from collections import deque


def bfs(i, j):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque([(i, j)])
    graph[i][j] = 0
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                count += 1

    return count


n, m, k = map(int, input().rstrip().split(" "))
graph = [[0] * m for _ in range(n)]

answer = 0
for _ in range(k):
    a, b = map(int, input().rstrip().split(" "))
    graph[a - 1][b - 1] = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            answer = max(answer, bfs(i, j))
print(answer)