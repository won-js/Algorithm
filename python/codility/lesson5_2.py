def solution(S, P, Q):
    result = []
    dna = list(S)

    length = len(dna)
    A = [0] * (length+1)
    C = [0] * (length+1)
    G = [0] * (length+1)

    for i in range(length):
        now = dna[i]
        if now == "A":
            A[i+1] += 1
        elif now == "C":
            C[i+1] += 1
        elif now == "G":
            G[i+1] += 1

        A[i+1] += A[i]
        C[i+1] += C[i]
        G[i+1] += G[i] 

    for i in range(len(P)):
        start = P[i]
        end = Q[i]+1

        if A[start] != A[end]:
            result.append(1)
        elif C[start] != C[end]:
            result.append(2)
        elif G[start] != G[end]:
            result.append(3)
        else:
            result.append(4)

    return result

print(solution("CAGCCTA",[2,5,0],[4,5,6]))