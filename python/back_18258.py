from collections import deque

n = int(input())
commands = []
queue = deque()

for _ in range(n):
    commands.append(input())

for command in commands:
    char = command[:2]

    if char == "pu":
        queue.append(int(command[5:]))
    elif char == "po":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif char == "si":
        print(len(queue))
    elif char == "em":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif char == "fr":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

