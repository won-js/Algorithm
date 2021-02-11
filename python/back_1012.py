import sys
sys.setrecursionlimit(10000)

t = int(input())

testcase = []
link = [[] for _ in range(t)]

for i in range(t):
    n, m, a = list(map(int, input().split(" ")))
    testcase.append([n,m,a])

    for _ in range(a):
        link[i].append(list(map(int, input().split(" "))))


def dfs(graph, x, y, n, m):
    if x < 0 or y < 0 or x >= n or y >= m or graph[x][y] == 0:
        return 0
    graph[x][y] = 0

    dfs(graph, x-1, y, n ,m)
    dfs(graph, x+1, y, n ,m)
    dfs(graph, x, y-1, n ,m)
    dfs(graph, x, y+1, n ,m)
    
    return 1


for i in range(len(testcase)):
    n, m, a = testcase[i]
    graph = [[0]*m for _ in range(n)]

    for j in range(a):
        x , y = link[i][j]
        graph[x][y] = 1

    count = 0
    for k in range(n):
        for g in range(m):
            count += dfs(graph, k, g, n, m)

    print(count)

