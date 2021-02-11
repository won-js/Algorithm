n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int,list(input()))))

m = len(graph[0])
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(graph, x, y, n, m):
    if x < 0 or y < 0 or x >= n or y >= m or graph[x][y] == 0:
        return 0

    graph[x][y] = 0
    count = 1

    for i in range(4):
        count += dfs(graph, x + dx[i], y + dy[i], n, m)

    return count

answer = []

for i in range(n):
    for j in range(m):
        count = dfs(graph,i,j,n,m)
        if count != 0:
            answer.append(count)

answer.sort()
print(len(answer))
for num in answer:
    print(num)
