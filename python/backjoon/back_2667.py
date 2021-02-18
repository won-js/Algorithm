import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input().rstrip())


def dfs(graph, x, y, count):
    if x < 0 or y < 0 or x >= n or y >= n:
        return 0
    if graph[x][y] == 0:
        return 0
    graph[x][y] = 0
    count += 1
    for i in range(4):
        count += dfs(graph, x + dx[i], y + dy[i], 0)
    return count


graph = []
for _ in range(n):
    graph.append(list(map(int, list(input().rstrip()))))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

answer = []
for i in range(n):
    for j in range(n):
        count = dfs(graph, i, j, 0)
        if count != 0:
            answer.append(count)
answer.sort()
print(len(answer))
for num in answer:
    print(num)