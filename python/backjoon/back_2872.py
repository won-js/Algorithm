import sys
input = sys.stdin.readline

n = int(input().rstrip())

books = []
for _ in range(n):
    books.append(int(input().rstrip()))

max_value = n
result = 0

for i in range(n-1,-1,-1):
    if books[i] == max_value:
        max_value -= 1
    else:
        result+=1

print(result)