first = True
answer = 0

string = input()
if string[0] == "-":
    first = False

arr = list(string.split("-"))

if first:
    answer += sum(list(map(int,arr[0].split("+"))))
else:
    answer -= sum(list(map(int,arr[0].split("+"))))

for i in range(1,len(arr)):
    answer -= sum(list(map(int,arr[i].split("+"))))

print(answer)