def solution(A):
    arr = [0] * 100001

    answer = 1

    for num in A:
        if num < 100001:
            arr[num] = 1

    for i in range(1,len(A)+1):
        if arr[i] == 0:
            return 0

    return answer   
