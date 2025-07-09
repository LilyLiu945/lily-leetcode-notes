class Solution:
    def reverseWords(self, s: str) -> str:
        
        # Convert the string to a list for in-place operations
        chars = list(s)
        
        # Step 1: Remove extra spaces
        def trim_spaces(chars):
            n = len(chars)
            left, right = 0, 0
            while right < n:
                # Skip leading spaces
                while right < n and chars[right] == ' ':
                    right += 1
                # Keep non-space characters
                while right < n and chars[right] != ' ':
                    chars[left] = chars[right]
                    left += 1
                    right += 1
                # Skip extra spaces between words
                while right < n and chars[right] == ' ':
                    right += 1
                # Add a single space if more words follow
                if right < n:
                    chars[left] = ' '
                    left += 1
            return chars[:left]

        # Step 2: Reverse characters from left to right
        def reverse(chars, left, right):
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        # Step 3: Reverse each word in the string
        def reverse_each_word(chars):
            n = len(chars)
            start = 0
            while start < n:
                end = start
                while end < n and chars[end] != ' ':
                    end += 1
                reverse(chars, start, end - 1)
                start = end + 1

        # Apply all steps
        trimmed = trim_spaces(chars)                     # Clean up spaces
        reverse(trimmed, 0, len(trimmed) - 1)            # Reverse entire string
        reverse_each_word(trimmed)                       # Reverse individual words
        return ''.join(trimmed)
