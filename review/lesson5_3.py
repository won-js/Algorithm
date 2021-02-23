def solution(A):
    N = len(A)
    min_value = int(1e9)
    answer = 0
    for i in range(len(A)-2):
        if min_value > (A[i]+A[i+1])/2:
            min_value = (A[i]+A[i+1])/2
            answer = i

        if min_value > (A[i]+A[i+1]+A[i+2])/3:
            min_value = (A[i]+A[i+1]+A[i+2])/3
            answer = i

    if min_value > (A[-1]+A[-2])/2:
        answer = len(A)-2

    return answer
