import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]


def dfs(x, y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return 0
    if graph[x][y] == 0:
        return 0
    graph[x][y] = 0
    for i in range(8):
        dfs(x + dx[i], y + dy[i])
    return 1


while True:
    w, h = map(int, input().rstrip().split(" "))
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().rstrip().split(" "))))

    answer = 0
    for i in range(h):
        for j in range(w):
            answer += dfs(i, j)
    print(answer)