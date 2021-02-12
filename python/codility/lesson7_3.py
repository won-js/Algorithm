def solution(S):
    stack = []

    for i in range(len(S)):
        char = S[i]

        if char == "(":
            stack.append(char)
        else:
            if stack:
                stack.pop()                
            else:
                return 0

    if stack:
        return 0

    return 1

print(solution("(()(())())"))