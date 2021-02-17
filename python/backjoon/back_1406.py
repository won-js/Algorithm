import sys
from collections import deque

input = sys.stdin.readline

s = input().rstrip()
n = int(input().rstrip())

left = deque()
right = deque()
for i in range(len(s)):
    left.append(s[i])

for _ in range(n):
    cmd = input().rstrip()
    if cmd == "L" and left:
        right.appendleft(left.pop())
    elif cmd == "D" and right:
        left.append(right.popleft())
    elif cmd == "B" and left:
        left.pop()
    elif cmd[0] == "P":
        left.append(cmd[2])

for st in left:
    print(st, end="")
for st in right:
    print(st, end="")
