from collections import deque
import sys

input = sys.stdin.readline

q = deque()
n = int(input().rstrip())
for _ in range(n):
    req = input()
    req2 = req[:2]
    if req2 == "pu":
        q.append(int(req[5:]))
    elif req2 == "po":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif req2 == "si":
        print(len(q))
    elif req2 == "em":
        if q:
            print(0)
        else:
            print(1)
    elif req2 == "fr":
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)