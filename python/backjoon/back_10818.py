n = int(input())
arr = list(map(int, input().split(" ")))

min_value = int(1e9)
max_value = -1*int(1e9)

for num in arr:
    min_value = min(min_value, num)
    max_value = max(max_value, num)

print(str(min_value)+ " "+str(max_value))

