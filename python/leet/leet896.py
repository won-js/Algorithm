class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        check = 0
        for i in range(1, len(A)):
            if check == 0:
                if A[i-1] < A[i]:
                    check = 1
                elif A[i-1] > A[i]:
                    check = -1
            else:
                if check == 1 and A[i-1] > A[i]:
                    return False
                elif check == -1 and A[i-1] < A[i]:
                    return False
        return True
