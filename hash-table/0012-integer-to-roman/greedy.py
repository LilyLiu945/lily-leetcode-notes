class Solution:
    def intToRoman(self, num: int) -> str:
        
        # value-symbol pairs in descending order, include subtractive forms
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        res = []
        for v, s in zip(vals, syms):
            cnt, num = divmod(num, v) # returns (num // v, num % v)
            res.append(s * cnt) # append s cnt times (maybe 0)
            if num == 0:
                break
            
        return "".join(res)
