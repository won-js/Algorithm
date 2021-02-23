class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sort_s = sorted(list(s))
        sort_t = sorted(list(t))

        for i in range(len(sort_s)):
            if sort_s[i] != sort_t[i]:
                return sort_t[i]

        return sort_t[-1]
