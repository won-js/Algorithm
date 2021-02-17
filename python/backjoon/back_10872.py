n = int(input())

answer = 1
for i in range(n, 0, -1):
    answer *= i
print(answer)