def solution(S):
    if not S:
        return 1
    stack = []
    for i in range(len(S)):
        char = S[i]
        if stack:
            if stack[-1] == "(" and char == ")":
                stack.pop()
            elif stack[-1] == "{" and char == "}":
                stack.pop()
            elif stack[-1] == "[" and char == "]":
                stack.pop()
            elif char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                return 0
        else:
            if char == ")" or char == "}" or char == "]":
                return 0
            else:
                stack.append(char)

    if stack:
        return 0
    else:
        return 1
