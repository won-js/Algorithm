strings = []

while True:
    temp = input()
    
    if temp == ".":
        break

    strings.append(temp)

for string in strings:
    stack = []
    boolean = True

    for i in range(len(string)):
        char = string[i]
        if char == ")" or char == "}" or char == "]" or char == "(" or char == "{" or char == "[":
            if len(stack) == 0:
                if char == ")" or char == "}" or char == "]":
                    boolean = False
                    break
                else:
                    stack.append(char)
            else:
                if char == ")" and stack[-1] == "(":
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                elif char == "(" or char == "{" or char == "[":
                    stack.append(char)
                else:
                    boolean = False
                    break
    
    if boolean and len(stack) == 0:
        print("yes")
    else:
        print("no")