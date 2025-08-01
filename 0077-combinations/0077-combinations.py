class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []

        def backtrack(start: int, path: List[int]):
            if len(path) == k:
                result.append(path[:])
                return

            # Pruning: Only loop until n - (k - len(path)) + 1
            # This ensures there are enough numbers left to fill the combination
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return result