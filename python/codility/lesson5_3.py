def solution(A):
    min_value = int(1e9)
    idx = 0

    # 평균값 계산
    for i in range(len(A)-2):
        avg = min((A[i]+A[i+1])/2 , (A[i]+ A[i+1]+A[i+2])/3)
        if min_value > avg:
            min_value = avg
            idx = i

    # 나머지 정리
    if min_value > (A[len(A)-2]+A[-1])/2:
        idx = len(A)-2

    return idx

print(solution([4,2,2,5,1,5,8]))