def solution(S, P, Q):
    N = len(S)
    A = [0] * (N+1)
    C = [0] * (N+1)
    G = [0] * (N+1)

    answer = []

    for i in range(N):
        now = S[i]
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
            answer.append(1)
        elif C[start] != C[end]:
            answer.append(2)
        elif G[start] != G[end]:
            answer.append(3)
        else:
            answer.append(4)

    return answer
