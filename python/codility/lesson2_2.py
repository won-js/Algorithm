def solution(A):
    map = {}
    
    for num in A:
        now = str(num)
        if now in map:
            map.pop(now)
        else:
            map[now] = 1
    
    for answer in map:
        return int(answer)

    return 0

