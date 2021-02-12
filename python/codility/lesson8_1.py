def solution(A):
    # dominator 을 담을 그릇
    domi = {}
    # election 의 개수 표시
    elec = {}
    # 총원
    total = len(A)

    for i in range(len(A)):
        now = A[i]
        if domi.get(now):
            domi.get(now).append(i)
            elec[now] = elec.get(now) + 1
        else:
            domi[now] = [i]
            elec[now] = 1

        ## 과반수 동의시 선거자중 한명 리턴
        if elec.get(now) > total//2:
            return domi.get(now)[0]

    return -1

print(solution([3,4,3,2,3,-1,3,3]))