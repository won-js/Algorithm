import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(" "))
graph = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(lsit(map(int, input().rstrip().split(" "))))

dx = [-1]