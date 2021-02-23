def solution(A, B, K):
    if A % K == 0:
        start = A
    else:
        start = A + (K-A % K)

    return (B-start)//K + 1
