import math
import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))
gcd = math.gcd(a, b)

while gcd != 0:
    gcd -= 1
    print(1, end="")
