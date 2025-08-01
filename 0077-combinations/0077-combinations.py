class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from typing import List
        result = []

        def backtrack(start: int, path: List[int]):
            # If the current combination is complete
            if len(path) == k:
                result.append(path[:])  # Append a copy of the current path
                return
            
            # Try all possible next candidates
            for i in range(start, n + 1):
                path.append(i)                  # Choose
                backtrack(i + 1, path)          # Explore with i+1 to ensure ascending order
                path.pop()                      # Unchoose (backtrack)
        
        backtrack(1, [])
        return result