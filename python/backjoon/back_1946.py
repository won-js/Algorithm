import sys
input = sys.stdin.readline

n = int(input())
emps = [[] for _ in range(n)]

for i in range(n):
    m = int(input())
    for _ in range(m):
        emps[i].append(list(map(int,input().split(" "))))


for emp in emps:
    count = 1
    emp_sort = sorted(emp, key= lambda x : x[1])

    bound = emp_sort[0][0]

    for i in range(1, len(emp_sort)):
        if bound > emp_sort[i][0]:
            count += 1
            bound = emp_sort[i][0]

    print(count)