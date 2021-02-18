import sys
from collections import deque

input = sys.stdin.readline


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def grouping(i, j):
    q = deque([(i, j)])
    graph[i][j] = group_id
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < n):
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = group_id
                elif graph[nx][ny] == 0:
                    ocean.append((x, y))
    return


## 모든 섬을 동시에 확장
def get_dist():
    loop = 0
    ans = int(1e9)
    while ocean:
        loop += 1
        length = len(ocean)
        for _ in range(length):
            x, y = ocean.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (0 <= nx < n) and (0 <= ny < n):
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]
                        ocean.append((nx, ny))
                    elif graph[nx][ny] < graph[x][y]:
                        ans = min(ans, (loop - 1) * 2)
                    elif graph[nx][ny] > graph[x][y]:
                        ans = min(ans, loop * 2 - 1)
    return ans


n = int(input().rstrip())
graph = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
ocean = deque()

group_id = -1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            grouping(i, j)
            group_id -= 1

print(get_dist())

## 참조 : https://suri78.tistory.com/133