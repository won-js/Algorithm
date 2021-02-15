def solution(s):
    length = len(s)
    answer = length

    for step in range(1, length // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1

        for j in range(step, length, step):
            if prev == s[j : j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j : j + step]
                count = 1

        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))

    return answer
