def solution(N):
    count = 0
    arr = [0]

    answer = toTwo(N)
    for i in range(1, len(answer)-1):
        if answer[i] == '0':
            count += 1
        else:
            arr.append(count)
            count = 0
    return max(arr)

def toTwo(N):
    answer = ""
    while N != 0:
        if N%2 == 0:
            answer = "0" + answer
        else:
            answer = "1" + answer
        N = N//2

    print(answer)
    return answer

print(solution(1041))