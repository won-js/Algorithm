def solution(H):
    
    # 처음 기둥을 넣고 카운트
    count = 1
    stack = [H[0]]

    for i in range(1,len(H)):
        # 현재 비교할 높이
        now = H[i]


        while stack:
            # 앞선 비교할 기둥 중 가장 큰 것과 비교
            # 더 크면 스택에 삽입
            if stack[-1] < now:
                count += 1
                stack.append(now)
                break
            elif stack[-1] == now:
                break
            else:
                # 현재 높이가 더 작으면 앞선 스택의 값들 삭제
                stack.pop()
                
        # 스택이 비게 되면 현재의 값 삽입
        if not stack:
            count += 1
            stack.append(now)
        
    return count

print(solution([8,8,5,7,9,8,7,4,8]))