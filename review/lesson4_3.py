def solution(A):
    arr = [False] * 1000001

    for num in A:
        if num <= 0:
            continue
        else:
            arr[num] = True

    for i in range(1, len(arr)):
        if not arr[i]:
            return i

    return 1000000
