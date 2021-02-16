string = input()
length = len(string)

left = 0
right = 0
half = length // 2

for i in range(length):
    if i < half:
        left += int(string[i])
    else:
        right += int(string[i])

if left == right:
    print("LUCKY")
else:
    print("READY")
