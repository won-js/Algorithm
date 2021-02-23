class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        answer = []
        dic = {}
        arr_sort = sorted(arr)

        rank = 1
        for num in arr_sort:
            if not dic.get(num):
                dic[num] = rank
                rank += 1

        for num in arr:
            answer.append(dic.get(num))

        return answer
