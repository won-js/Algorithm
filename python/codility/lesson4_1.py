def solution(X,A):
    visited = [ 0 ] * (X+1)
    answer = -1

    total = 0
    for i in range(len(A)):
        leaf = A[i]
        
        if visited[leaf] == 0:
            total += 1
            visited[leaf] = 1

        if total == X:
            answer = i
            break
    
    return answer
