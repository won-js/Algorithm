import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())

nations = []
for i in range(t):
    n, m = map(int, input().rstrip().split(" "))
    nations.append([[] for _ in range(n + 1)])
    for _ in range(m):
        nation1, nation2 = map(int, input().rstrip().split(" "))
        nations[i][nation1].append(nation2)
        nations[i][nation2].append(nation1)


def bfs(visited, start, nation):
    q = deque()
    visited[start] = True
    count = 0
    for a in nation[start]:
        q.append(a)
    while q:
        now = q.popleft()
        if not visited[now]:
            count += 1
            visited[now] = True
            for a in nation[now]:
                q.append(a)
    return count


for i in range(t):
    leng = len(nations[i])
    visited = [False] * (leng + 1)
    print(bfs(visited, 1, nations[i]))
