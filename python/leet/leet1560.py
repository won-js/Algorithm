class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        visited = [0] * (n+1)
        visited[rounds[0]] += 1
