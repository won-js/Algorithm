def solution(A):

    left = A[0]
    total = sum(A)

    min_value = abs(2*left - total)
    
    for i in range(1,len(A)-1):
        left += A[i]
        current = abs(2*left - total)
        if min_value > current:
            min_value = current
        
    return min_value

