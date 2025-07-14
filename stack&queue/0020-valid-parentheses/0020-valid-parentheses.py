class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(',']':'[','}':'{'}

        for i in s:
            if i in mapping: # Right parenthesis
                if not stack or stack[-1] != mapping[i]:
                    return False
                stack.pop() 
            else: # Left parenthesis
                stack.append(i)
            
        return not stack
