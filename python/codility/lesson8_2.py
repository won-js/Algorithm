def solution(A):
    count = 0
    for i in range(len(A) - 1):
        if elec(A[: i + 1]) == elec(A[i + 1 :]):
            count += 1
    return count


# def elec(arr):
#     dic = {}
#     for num in arr:
#         if not dic.get(num):
#             dic[num] = 1
#         else:
#             dic[num] = dic.get(num) + 1

#     for key, value in dic.items():
#         if value > len(arr) // 2:
#             return key

#     return None
def elec(arr):
    n = len(arr)
    size = 0
    for i in range(n):
        if size == 0:
            size += 1
            value = arr[i]
        else:
            if value != arr[i]:
                size -= 1
            else:
                size += 1
    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0
    for i in range(n):
        if arr[i] == candidate:
            count += 1
        if count > n // 2:
            leader = candidate
        return leader