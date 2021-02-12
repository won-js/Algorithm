def solution(A,B):
    # 위로 가는 물고기와 아래로 가는 물고기를 담을 그릇
    down = []
    up = []

    # 살아남은 물고기 수
    count = 0

    for i in range(len(A)):

        # 위로 가는 건 up , 아래로 가는 건 down으로    
        if B[i] == 0:
            up.append(A[i])
        else:
            down.append(A[i])

        # 물고기들의 만남
        while up and down:
            if up[-1] > down[-1]:
                down.pop() # down 물고기 잡아먹힘
            else:
                up.pop() # up 물고기 잡아 먹힘
            # 둘 중 전멸할때 까지

        # 내려오는 물고기가 없으면 up 지금까지 위로 가는 물고기는 모두 생존
        if not down:
            while up:
                count += 1
                up.pop()
        
    # 끝까지 와서 내려오는 물고기가 남아 있으면 모두 생존
    while down:
        count += 1
        down.pop()

    return count
