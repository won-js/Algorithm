s = input()

alpha = [0] * 26

for i in range(len(s)):
    alpha[ord(s[i]) - 97] += 1

for a in alpha:
    print(a, end=" ")