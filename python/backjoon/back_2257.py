s = input()

stack = []

for i in range(len(s)):
    char = s[i]

    if char == "H":
        stack.append(1)

    elif char == "C":
        stack.append(12)

    elif char == "O":
        stack.append(16)
    elif char == "(":
        stack.append("(")
    elif char == ")":
        temp = 0
        while stack[-1] != "(":
            temp += stack.pop()
        stack.pop()
        stack.append(temp)
    else:
        temp = stack.pop()
        stack.append(temp * int(char))

print(sum(stack))