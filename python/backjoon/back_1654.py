n, m = map(int, input().split(" "))

array = []
for _ in range(n):
    array.append(int(input()))

start = min(array)
end = max(array)


def cut(arr, n):
    count = 0
    mid = (start + end) // 2
    for i in range(len(arr)):
        count += arr[i] // n
    return count


max_value = 0
while True:
    mid = (start + end) // 2
    count = cut(array, mid)
    if count < m:
        end = mid
    elif count > m:
        start = mid
    else:
        print(mid)
        break