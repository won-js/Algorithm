people = 0
max_value = 0

for _ in range(10):
    off, on = map(int, input().split(" "))
    people = people + on - off 
    max_value = max(max_value, people)

print(max_value)