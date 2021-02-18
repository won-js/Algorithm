s = input()

for i in range(len(s)):
    now = ord(s[i])
    if now >= 65 and now <= 90:
        now += 13
        if now > 90:
            now -= 26
    elif now >= 97 and now <= 122:
        now += 13
        if now > 122:
            now -= 26

    print(chr(now), end="")