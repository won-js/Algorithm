def solution(food_times, k):
    total = sum(food_times)
    if total < k:
        return -1
    
    time = 0
    idx = 0
    max_idx = len(food_times)
    while True:
        if idx >= max_idx:
            idx = 0
        if time == k:
            return idx +1

        if total == 0:
            return -1

        if food_times[idx] != 0:
            food_times[idx] -= 1
            total -= 1
            time += 1

        idx += 1

print(solution([3,1,2,],5))
