n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    node1, node2 = list(map(int,input().split(" ")))
    graph[node1].append(node2)
    graph[node2].append(node1)

def dfs(graph, visited, start):
    visited[start] = True
    global count
    count += 1

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i)
    

visited = [False] * (n+1)
count = 0
dfs(graph, visited, 1)
print(count-1)
