class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        answer = 0
        for i in range(len(s)-1):
            start = s[i]
            my , you = 1 , 0
            for j in range(i+1,len(s)):
                if start == s[j]:
                    my += 1
                else:
                    you += 1

                if my == you:
                    answer += 1
                    break
        return answer
