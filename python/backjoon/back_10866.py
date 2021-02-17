import sys
from collections import deque

input = sys.stdin.readline
q = deque()
n = int(input().rstrip())

for _ in range(n):
    req = input().rstrip()
    req2 = req[:2]
    if req2 == "pu":
        if req[5] == "f":
            q.appendleft(int(req[11:]))
        else:
            q.append(int(req[10:]))
    elif req2 == "po":
        if req[4] == "f":
            if q:
                print(q.popleft())
            else:
                print(-1)
        else:
            if q:
                print(q.pop())
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
