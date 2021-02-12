n = int(input())

testcase = []
for _ in range(n):
    testcase.append(int(input()))

for case in testcase:
    binary = format(case, 'b')
    
    idx = 0
    for i in binary[::-1]:
        if i == '1':
            print(idx,end=" ")
        idx += 1

    print()
 