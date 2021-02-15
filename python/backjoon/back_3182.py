import sys

input = sys.stdin.readline

n = int(input().rstrip())

matrix = [[0] * (n + 1) for _ in range(n + 1)]

print(matrix)