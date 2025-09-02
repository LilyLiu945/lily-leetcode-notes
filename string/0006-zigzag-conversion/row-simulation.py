class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Build the zigzag row by row while moving a pointer up and down.
        Time:  O(n) — visit each char once
        Space: O(n) — to store rows before joining
        """
        
        n = len(s)
        # Trivial cases: no zigzag needed.
        if numRows == 1 or numRows >= n:
            return s

        rows = [""] * numRows
        row = 0          # current row index
        dir = 1          # +1 going down, -1 going up

        for ch in s:
            rows[row] += ch
            # Flip direction at the top/bottom row.
            if row == 0:
                dir = 1
            elif row == numRows - 1:
                dir = -1
            row += dir

        return "".join(rows)
