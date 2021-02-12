from collections import deque

def solution(A,K):
    if not A:
        return A
    q = deque(A)
    for _ in range(K):
        q.appendleft(q.pop())
    return [i for i in q]