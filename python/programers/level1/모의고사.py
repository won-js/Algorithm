def solution(answers):
    first = [1,2,3,4,5] * (10000//5)
    second = [2,1,2,3,2,4,2,5] * (10000//8)
    third = [3,3,1,1,2,2,4,4,5,5] * (10000//10)

    correct = [0,0,0]
    for i in range(len(answers)):
        if first[i] == answers[i]:
            correct[0] += 1
        if second[i] == answers[i]:
            correct[1] += 1
        if third[i] == answers[i]:
            correct[2] += 1

    max_value = max(correct)

    result = []
    for i in range(len(correct)):
        if(max_value == correct[i]):
            result.append(i+1)
    
    return result
