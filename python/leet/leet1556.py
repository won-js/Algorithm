class Solution:
    def thousandSeparator(self, n: int) -> str:
        answer = ""
        arr = list(str(n))

        n = 0
        for i in range(len(arr)-1, -1, -1):
            if n % 3 == 0 and n != 0:
                answer = "."+answer
            answer = arr[i] + answer
            n += 1

        return answer
