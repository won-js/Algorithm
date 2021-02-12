def solution(A):
    in_number = [0] * (len(A)+2)
    
    for num in A:
        in_number[num] = 1

    for i in range(1,len(in_number)):
        if 0 == in_number[i]:
            return i

    return 0

print(solution([2,3,1,5]))