def solution(A):
    arr = [False] * 100001

    for num in A:
        if num <= 100000:
            if arr[num]:
                return 0
            else:
                arr[num] = True

    for i in range(1, len(A)+1):
        if not arr[i]:
            return 0
    return 1
