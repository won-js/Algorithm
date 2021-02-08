n = int(input())
arr = list(map(int,input().split(" ")))

result = 0
count = 0
arr_sort = sorted(arr)

for num in arr_sort:
    count += num
    result += count

print(result)