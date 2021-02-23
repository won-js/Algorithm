def solution(A):
    s = set()

    for num in A:
        if num in s:
            s.remove(num)
        else:
            s.add(num)

    return s.pop()


print(solution([9,3,9,3,9,7,9]))