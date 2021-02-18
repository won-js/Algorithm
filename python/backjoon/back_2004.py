def count(n, k):
    result = 0
    while n != 0:
        n = n // k
        result += n
    return result

n, m = map(int, input().split(" "))

print(min(count(n,2)- count(m,2)- count(n-m,2) , count(n,5)- count(m,5)- count(n-m,5)))