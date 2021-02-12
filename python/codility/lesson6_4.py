def solution(A):
    A_sort = sorted(A)

    for i in range(len(A)-2):
        if A_sort[i]+A_sort[i+1] > A_sort[i+2]:
            return 1

    return 0