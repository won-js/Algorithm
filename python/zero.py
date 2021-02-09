n = int(input())

stack = []
answers = []

for _ in range(n):
    answers.append(int(input()))

for answer in answers:
    if answer == 0:
        stack.pop()
    else:
        stack.append(answer)

print(sum(stack))