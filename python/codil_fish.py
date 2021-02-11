# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    upstream = []
    downstream =[]
    result = 0 
    # start = 0
    # end = len(A)

    # for i in range(len(A)):
    #     if B[i] == 0:
    #         result += 1
    #     else:
    #         start = i
    #         break
                 
    # for i in range(len(A)-1,-1,-1):
    #     if B[i] == 1:
    #         result += 1
    #     else:
    #         end = i
    #         break
    
    for i in range(len(A)):
        if B[i] == 0:
            upstream.append(A[i])
        else:
            downstream.append(A[i])

        while True:
            if not upstream or not downstream:
                break
            else:
                if upstream[-1] < downstream[-1]:
                    upstream.pop()
                else:
                    downstream.pop()

        
        if not downstream:
            while upstream:
                upstream.pop()
                result += 1

    if not upstream:
        while downstream:
            downstream.pop()
            result += 1
    
    return result
            
print(solution([4,3,2,1,5],[0,1,0,0,0]))