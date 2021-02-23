def solution(A):
    visited = [False] * (len(A)+2)

    for num in A:
        visited[num] = True

    for i in range(1,len(visited)):
        if not visited[i]:
            return i
    return 0
