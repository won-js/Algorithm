def solution(N):
    binary = format(N,'b')

    max_value = 0
    count = 0
    for i in range(1,len(binary)):
        now = binary[i]        
        if now == '1':
            max_value = max(max_value,count)
            count = 0
        else:
            count += 1

    return max_value