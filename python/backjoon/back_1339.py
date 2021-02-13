import sys
input = sys.stdin.readline

n = int(input())
array = []
dic = {}
num = 9

for _ in range(n):
    array.append(list(input().rstrip()))

def change_int(S):
    answer = ""
    global num
    for string in S:
        if dic.get(string):
            integer = dic.get(string)
        else:
            dic[string] = num
            integer = num
            num -= 1
        answer += str(integer)
    print(answer)
    return answer

array = sorted(array, key = lambda x : len(x), reverse=True)

result = 0

for i in range(len(array)):
    result += int(change_int(array[i]))

print(result)


