n = int(input())
commands = []
for _ in range(n):
    commands.append(input())

stack = []

for command in commands:
    check = command[:2]
    if check == "pu":
        stack.append(command[5:])
    elif check == "po":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif check == "si":
            print(len(stack))
    elif check == "em":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])