n = int(input())

ropes = []

for _ in range(n):
    ropes.append(int(input()))

if n == 1:
    print(ropes[0])
else:
    ropes.sort()
    
    max_value = 0
    length = 1 

    for i in range(n-1,-1,-1):
        max_value = max(max_value,ropes[i]*length)
        length += 1

    print(max_value)