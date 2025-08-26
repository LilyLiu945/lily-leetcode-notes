class Solution:
    def intToRoman(self, num: int) -> str:
        
        thousands = ["", "M", "MM", "MMM"]  # 0..3
        hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]  # 0..9
        tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]  # 0..9
        ones      = ["", "I", "II", "III", "IV","V","VI","VII","VIII","IX"]       # 0..9

        # split into thousands, hundreds, tens, ones
        th = num // 1000
        h = (num % 1000) // 100
        t = (num % 100) // 10
        o = num % 10

        return thousands[th] + hundreds[h] + tens[t] + ones[o]
