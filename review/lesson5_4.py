def solution(A):
    curr = 0
    passing = 0

    for car in A:
        if car == 0:
            curr += 1
        else:
            passing += curr

        if passing > 1000000000:
            return -1

    return passing
