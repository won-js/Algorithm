def solution(A):
    # 총 만난 대수
    result = 0
    # 만나기로 예정된 대수
    now = 0

    for car in A:
        if car == 0:
            now += 1
        else:
            result += now
        
        if result > 1000000000:
            return -1

    return result

print(solution([0,1,0,1,1]))