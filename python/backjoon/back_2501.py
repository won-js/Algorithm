n, m = map(int, input().split(" "))

array = []
answer = 0

for i in range(1, n+1):
    if n%i == 0:
        array.append(i)

if m <= len(array):
    answer = array[m-1]

print(answer)