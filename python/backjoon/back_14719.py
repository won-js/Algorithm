n, m = map(int, input().split(" "))
ground = list(map(int, input().split(" ")))

left = [0] * m
right = [0] * m

# 오른쪽으로 갈 때 채우기
max_value = 0
for i in range(m):
    if max_value < ground[i]:
        max_value = ground[i]
    right[i] = max_value

# 왼쪽으로 갈 때
max_value = 0
for i in range(m-1,-1,-1):
    if max_value < ground[i]:
        max_value = ground[i]
    left[i] = max_value

count = 0
for i in range(m):
    count += min(left[i],right[i]) - ground[i]

print(count)