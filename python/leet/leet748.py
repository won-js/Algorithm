class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        arr_sort = sorted(arr, key=lambda x: len(x))

        for word in words:
            dic = {}
            check = False
            makeDict(word)

            for char in list(licensePlate):
                


    def makeDict(string):
        for char in list(string):
            if dic.get(char):
                dic[char] += 1
            else:
                dic[char] = 1