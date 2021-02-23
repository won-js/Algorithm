def solution(N,A):
    dic = {}
    curr_max = 0
    total_max = 0

    for num in A:
        if num == N+1:
            total_max += curr_max
            curr_max = 0
            dic.clear()
        else:
            if dic.get(num):
                dic[num] += 1
                if dic[num] > curr_max:
                    curr_max = dic[num]
            else:
                dic[num] = 1
                if curr_max < 1:
                    curr_max = 1
    
    answer = [total_max] * (N)

    for i in dic.keys():
        answer[i-1] += dic[i]

    return answer