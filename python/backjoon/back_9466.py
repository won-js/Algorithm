import sys

sys.setrecursionlimit(10000000)
input = sys.stdin.readline

t = int(input().rstrip())


def dfs(start):
    global answer
    visited[start] = True
    loop.append(start)
    after = arr[start]

    if visited[after]:
        if after in loop:
            answer += loop[loop.index(after) :]
        return
    else:
        dfs(after)


for _ in range(t):
    n = int(input().rstrip())
    arr = [0] + list(map(int, input().rstrip().split(" ")))

    visited = [False] * (n + 1)

    answer = []
    for i in range(1, n + 1):
        if not visited[i]:
            loop = []
            dfs(i)

    print(n - len(answer))