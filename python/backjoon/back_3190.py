import sys

input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())

board = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().rstrip().split(" "))
    board[x][y] = 1

m = int(input().rstrip())
dir = []

for _ in range(m):
    after, direction = input().rstrip().split(" ")
    dir.append((int(after), direction))

print(dir[0][0])