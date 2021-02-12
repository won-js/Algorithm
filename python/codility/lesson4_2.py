def solution(N, A):
    result = [0] * N

    dict = {}

    max_value = 0
    curr_max = 0

    for i in range(len(A)):
        if A[i] == N+1:
            dict.clear()
            max_value += curr_max
            curr_max = 0
        else:
            if(dict.get(A[i])):
                temp = dict.get(A[i]) + 1
                dict[A[i]] = temp
                if(curr_max < temp):
                    curr_max = temp 
            else:
                dict[A[i]] = 1
                if(curr_max < 1):
                    curr_max =1

    for i in range(len(result)):
        result[i] = max_value

    for i in dict.keys():
        result[i-1] += dict.get(i)

    return result

print(solution(5, [3,4,4,6,1,4,4]))