# Solution: Monotonic Decreasing Stack (store indices)
# 
# The stack stores "indices", not actual temperatures.
# However, the "monotonicity" refers to the temperatures corresponding to those indices.
# That is, temperatures[stack[-1]] is decreasing from bottom to top.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day
            stack.append(i)
        return answer
