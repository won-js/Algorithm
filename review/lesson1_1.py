def solution(N):
    arr = list(str(format(N, 'b')))

    max_value = 0
    count = 0
    for i in range(1, len(arr)):
        if arr[i] == "0":
            count += 1
        else:
            max_value = max(max_value, count)
            count = 0

    return max_value


print(solution(1041))
