def solution(A):
    A_sort = sorted(A)
    left = A_sort[0] * A_sort[1] * A_sort[-1]
    right = A_sort[-1] * A_sort[-2] * A_sort[-3]

    return max(left,right)
