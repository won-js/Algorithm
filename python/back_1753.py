import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수 , 간선 개수
n, m = map(int, input().split(" "))
# 시작 노드
v = int(input())

# graph, distance, visited
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
visited = [False] * (n+1)

# graph 채우기
for _ in range(m):
    node1, node2, cost = map(int, input().split(" "))
    graph[node1].append((node2,cost))

# 다익스트라
def dijkstra(start):
    q = []
    # 시작 노드로 가기 윈한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 도드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

# 실행
dijkstra(v)

for i in range(1,n+1):
    if distance[i] != int(1e9):
        print(distance[i])
    else:
        print("INF")