from collections import deque

n, m, v = list(map(int,input().split(" ")))

graph = [[] for _ in range(n+1)]

for _ in range(m):
    node1, node2 = list(map(int, input().split(" ")))
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(len(graph)):
    graph[i].sort()
    
## dfs
def dfs(graph, start, visited, answer):
    visited[start] = True
    answer += str(start) + " "

    for i in graph[start]:
        if not visited[i]:
            answer = dfs(graph, i, visited, answer)
    
    return answer

visited = [False] * (n+1)
answer = dfs(graph, v, visited, "")
print(answer)

## bfs
def bfs(graph, start, visited, answer):
    visited[start] = True
    queue = deque([start])

    while queue:
        # 큐에서 하나의 원소 출력
        v = queue.popleft()
        answer += str(v) + " "
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return answer

visited = [False] * (n+1)
answer = bfs(graph, v, visited, "")
print(answer)
