n = int(input())

strings = []

for _ in range(n):
    strings.append(input())

for string in strings:
    boolean = True
    stack = []
    for i in range(len(string)):
        char = string[i]
        if len(stack) == 0:
            if char == ")":
                boolean = False
                break
            else:
                stack.append(char)
        else:
            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == ")" and stack[-1] == ")":
                boolean = False
                break
            else:
                stack.append(char)

    if boolean and len(stack) == 0:
        print("YES")
    else:
        print("NO")