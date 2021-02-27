def solution(S):
    if not S:
        return 1

    N = len(S)

    stack = []

    for i in range(N):
        char = S[i]
        if stack:
            if char == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return 0
            else:
                stack.append(char)
        else:
            if char == ")":
                return 0
            else:
                stack.append(char)

    if stack:
        return 0
    else:
        return 1
