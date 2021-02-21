import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input().rstrip())

graph = [[0] * (n+1) for _ in range(n+1)]

for 