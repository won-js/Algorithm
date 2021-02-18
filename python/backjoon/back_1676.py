import math

n = int(input())

s = str(math.factorial(n))

count = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == "0":
        count += 1
    else:
        break
print(count)