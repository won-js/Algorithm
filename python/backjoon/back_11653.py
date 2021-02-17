import sys

input = sys.stdin.readline

n = int(input().rstrip())

if n != 1:
    div = 2
    while n != 1:
        if n % div == 0:
            print(div)
            n = n // div
        else:
            div += 1
