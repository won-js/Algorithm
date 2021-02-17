def solution(A):
    length = len(A)
    answer = 0
    for i in range(1,length-1):
        for j in range(i,length):
            answer = max(answer,cut(A[:i]) + cut(A[i+1:j]))
    return answer

def cut(arr):
    max_ending = max_slice = 0
    for a in arr:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice