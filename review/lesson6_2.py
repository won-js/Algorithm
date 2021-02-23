def solution(A):
    A_sort = sorted(A)
    return max(A_sort[0]*A_sort[1]*A_sort[2], A_sort[-3]*A_sort[-2]*A_sort[-1])
