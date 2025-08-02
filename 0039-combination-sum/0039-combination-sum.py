class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Optional but helpful for pruning

        def backtrack(start: int, path: List[int], total: int):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return # Exceeded the target, stop

            for i in range(start, len(candidates)):
                num = candidates[i]
                if total + num > target:
                    break  # Prune: further numbers will only be larger

                path.append(num)
                backtrack(i, path, total + num)  # Not i+1 because we can reuse same number
                path.pop()

        backtrack(0, [], 0)
        return result