import sys

from collections import deque

input = sys.stdin.readline

n, k = map(int, input().rstrip().split(" "))


def bfs(n, k):
    if n == k:
        return 0, 1
    if n > k:
        return n - k, 1

    INF = int(1e9)
    q = deque([n])
    visited = [INF] * 100001
    method = [0] * 100001
    time = 0
    stop = False

    method[n] = 1
    visited[n] = 0

    while q and not stop:
        length = len(q)

        for _ in range(length):
            now = q.popleft()

            for next in (now - 1, now + 1, now * 2):
                if next >= 0 and next <= 100000 and time + 1 <= visited[next]:
                    method[next] += 1
                    visited[next] = time + 1

                    if next == k:
                        stop = True

                    if not stop:
                        q.append(next)
        time += 1

    return visited[k], method[k]


time, count = bfs(n, k)
print(time)
print(count)
