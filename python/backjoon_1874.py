n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

boolean = []
stack = []
idx = 0
count = 0

for i in range(1,n+1):
    stack.append(i)
    boolean.append("+")
    count += 1

    if i == arr[idx]:
        while len(stack) != 0:
            if stack[-1] == arr[idx]:
                stack.pop()
                boolean.append("-")
                count -= 1
                idx += 1
            else:
                break

if count == 0:
    for char in boolean:
        print(char)
else:
    print("NO")    
    