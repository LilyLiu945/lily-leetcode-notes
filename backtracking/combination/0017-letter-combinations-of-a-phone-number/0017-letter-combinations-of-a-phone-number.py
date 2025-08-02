class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping from digit to corresponding letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index: int, path: str):

            # If the current path is complete
            if index == len(digits):
                result.append(path)
                return

            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            letters = phone_map[current_digit]

            # Try each letter for this digit
            for letter in letters:
                backtrack(index + 1, path + letter)

        # Start backtracking from the first digit
        backtrack(0, "")
        return result
