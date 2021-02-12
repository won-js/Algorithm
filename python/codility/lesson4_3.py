def solution(A):
    arr = [0] * 1000001
    answer = 1

    for num in A:
        if num > 0:
            arr[num] = 1
    
    for i in range(1,1000001):
        if arr[i] == 0:
            answer = i
            break

    return answer

