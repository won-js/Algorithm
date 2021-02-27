def solution(A, B):
    up = []
    down = []
    answer = 0

    for i in range(len(A)):
        if B[i] == 0:
            up.append(A[i])
        else:
            down.append(A[i])

        while up and down:
            if up[-1] > down[-1]:
                down.pop()
            else:
                up.pop()

        if not down:
            answer += len(up)
            up.clear()

    if down:
        answer += len(down)

    return answer
