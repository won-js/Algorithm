n = int(input())
m = list(map(int, input().split(" ")))

count = 0

if len(m) == n:
    for i in m:
        res = 0
        for j in range(1, i+1):
            if i % j == 0:
                res += 1
            if res > 2:
                break
        if res == 2:
            count += 1

print(count)