from collections import deque

n, m = list(map(int, input().split(" ")))

graph = []

for _ in range(n):
    graph.append(list(map(int,list(input()))))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        