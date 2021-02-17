s = input()

stack = []
count = 0
for i in range(len(s)):
    char = s[i]
    if char == "(":
        stack.append(char)
    else:
        stack.pop()
        if s[i - 1] == "(":
            count += len(stack)
        else:
            count += 1

print(count)