n = int(input())

testcase = []

for _ in  range(n):
    testcase.append(list(map(int, input().split(" "))))

for case in testcase:
    case.sort()
    print(case[7])
