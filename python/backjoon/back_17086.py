import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(" "))

graph = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]


def bfs(shark):
    step = 0
    dx = [1, 1, 1, -1, -1, -1, 0, 0]
    dy = [1, -1, 0, 1, -1, 0, 1, -1]
    while shark:
        length = len(shark)
        step += 1
        for _ in range(length):
            x, y = shark.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 0:
                    shark.append((nx, ny))
                    graph[nx][ny] = step


shark = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            shark.append((i, j))

bfs(shark)

max_value = 0
for i in range(n):
    for j in range(m):
        max_value = max(max_value, graph[i][j])
print(max_value)