start, end = map(int, input().split(" "))

arr = []
for i in range(1, end+1):
    for _ in range(i):
        arr.append(i)

print(sum(arr[start-1:end]))
