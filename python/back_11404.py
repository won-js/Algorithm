INF = int(1e9)

#  노드개수
n = int(input())
#  간선개수
m = int(input())

# graph
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용 0
for i in range(1,n+1):
    graph[i][i] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split(" "))
    # 출발 도시와 도착도시가 같은 노선이 있을 수 있음
    graph[a][b] = min(graph[a][b], c)

# 플로이드 위셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

for a in range(1,n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
        
    print()