import sys

input = sys.stdin.readline

n = int(input().rstrip())
a, b = map(int, input().rstrip().split(" "))

dow = int(input().rstrip())
topping = []

for _ in range(n):
    topping.append(int(input().rstrip()))

topping.sort(reverse=True)

result = dow // a
kal = dow

for i in range(n):
    kal += topping[i]
    now = kal // (a + (i + 1) * b)
    if result > now:
        break
    else:
        result = now

print(result)