class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def getNextValidCharIndex(txt, index):
            skip = 0
            while index >= 0:
                if txt[index] == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    break
                index -= 1
            return index

        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = getNextValidCharIndex(s, i)
            j = getNextValidCharIndex(t, j)

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1

        return True


            

             
        