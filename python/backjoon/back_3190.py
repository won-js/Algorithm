import sys

input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())

board = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().rstrip().split(" "))
    board[x][y] = 1

m = int(input().rstrip())
future = []

for _ in range(m):
    after, direction = input().rstrip().split(" ")
    future.append((int(after), direction))

head = [0,0]
tail = [0,0]
count = 0
idx = 0


while True:
    count+=1
    if count = future[idx][0]:
        idx += 1
        char = future[idx][1]

        