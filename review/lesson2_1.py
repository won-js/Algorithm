from collections import deque


def solution(A, K):
    if not A:
        return []

    q = deque(A)
    for _ in range(K):
        q.appendleft(q.pop())

    answer = []
    while q:
        answer.append(q.popleft())

    return answer


solution([3, 8, 9, 7, 6], 3)
