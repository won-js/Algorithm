def solution(A):

    left = A[0]
    total = sum(A)

    min_value = abs(2*left - total)
    for i in range(1, len(A)-1):
        left += A[i]
        min_value = min(min_value, abs(2*left - total))

    return min_value
