def solution(A):
    array = set()

    for num in A:
        array.add(num)

    return len(array)

print(solution([1,2,3,1,2,3]))