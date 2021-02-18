import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(x, y, count):
    if x < 0 or y < 0 or x >= n or y >= m:
        return 0
    if graph[x][y] == 0:
        return 0
    count += 1
    graph[x][y] = 0
    for i in range(4):
        count += dfs(x + dx[i], y + dy[i], 0)
    return count


graph = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().rstrip().split(" "))
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split(" "))))

answer = []
for i in range(n):
    for j in range(m):
        count = dfs(i, j, 0)
        if count != 0:
            answer.append(count)
print(len(answer))
if answer:
    print(max(answer))
else:
    print(0)