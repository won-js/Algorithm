from collections import deque

n, m = list(map(int, input().split(" ")))

graph = []

for _ in range(n):
    graph.append(list(map(int,list(input()))))


dx = [-1,1,0,0]
dy = [0,0,-1,1]
# bfs 구현
def bfs(x,y):
    # 큐 구현을 위한 deque 사용
    queue = deque()
    queue.append((x,y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0 or nx >= n or ny >= m :
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))
