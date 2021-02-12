heights = []

for _ in range(9):
    heights.append(int(input()))

heights.sort()
total = sum(heights)
first = 0
second = 0

for i in range(8):
    for j in range(i+1,9):
        if total - heights[i] - heights[j] == 100:
            first = i
            second = j
            break

for i in range(9):
    if i != first and i != second:
        print(heights[i])