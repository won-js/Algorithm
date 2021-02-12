def solution(S):
    stack = []

    for i in range(len(S)):
        char = S[i]
        if stack:
            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                return 0
        else:
            if char == ")" or char == "]" or char == "}":
                return 0
            else:
                stack.append(char)
        
    if stack:
        return 0

    return 1

print(solution( "{[()()]}"))