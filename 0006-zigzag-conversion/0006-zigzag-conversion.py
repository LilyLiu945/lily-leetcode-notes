class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n, R = len(s), numRows
        if R == 1 or R >= n:
            return s

        cycle = 2 * (R - 1)
        res = []

        for r in range(R):
            for i in range(r, n, cycle):
                res.append(s[i])

                j = i + (cycle - 2 * r)
                if 0 < r < R - 1 and j < n:
                    res.append(s[j])

        return "".join(res)