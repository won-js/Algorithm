import sys
from collections import deque

input = sys.stdin.readline


def bfs(i, j, team):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque([(i, j)])
    graph[i][j] = 0
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < m) and (0 <= ny < n) and graph[nx][ny] == team:
                count += 1
                graph[nx][ny] = 0
                q.append((nx, ny))
    return count ** 2


n, m = map(int, input().rstrip().split(" "))

graph = [list(input().rstrip()) for _ in range(m)]

w = 0
b = 0
for i in range(m):
    for j in range(n):
        now = graph[i][j]
        if now == "W":
            w += bfs(i, j, "W")
        elif now == "B":
            b += bfs(i, j, "B")

print(w, b)
