import math

n, m = map(int, input().split(" "))

gcd = math.gcd(n, m)
lcm = (n*m)//gcd

print(gcd)
print(lcm)