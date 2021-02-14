n , l = map(int,input().split(" "))

leak = list(map(int, input().split(" ")))

leak.sort()

blocked = [False] * n
result = 0

for i in range(n):
    if blocked[i]:
        continue
    
    idx = 0
    total = 0

    while i+idx < n:
        total = leak[i+idx] - leak[i] + 1
        if total <= l:
            blocked[i+idx] = True
            idx += 1
        else:
            break
    
    result += 1

print(result)