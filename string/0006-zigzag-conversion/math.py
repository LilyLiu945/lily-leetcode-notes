class Solution:
    def convert(self, s: str, numRows: int) -> str:
         """
        Use arithmetic indices per row.
        One "zigzag cycle" has length cycle = 2*(numRows-1).
        For row r:
          - take indices i = r, r+cycle, r+2*cycle, ...
          - if 0<r<numRows-1, also take i + (cycle - 2*r) inside the same cycle.
        Time:  O(n)
        Space: O(n)
        """
        
        n, R = len(s), numRows
        if R == 1 or R >= n:
            return s

        cycle = 2 * (R - 1)
        res = []

        for r in range(R):
            # Vertical hits: once per cycle
            for i in range(r, n, cycle):
                res.append(s[i])
                
                # Diagonal hits: only for middle rows, once per cycle
                j = i + (cycle - 2 * r)
                if 0 < r < R - 1 and j < n:
                    res.append(s[j])

        return "".join(res)
