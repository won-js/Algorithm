from collections import deque

n = int(input())

testcase = []
prior = []
for _ in range(n):
    testcase.append(list(map(int,input().split(" "))))
    prior.append(list(map(int,input().split(" "))))

for i in range(len(testcase)):
    N, M = testcase[i]
    queue = deque()
    idx = deque()

    # 그릇 만들기
    for i in range(N):
        queue.append(prior[i])
        idx.append(i)n

    maximum = max(queue)
    count = 0

    while true:
        if maximum == queue[0]:
            queue.popleft()
            idx.popleft()

