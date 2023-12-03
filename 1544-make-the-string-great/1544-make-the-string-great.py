class Solution:
    def makeGood(self, s: str) -> str:
        k = 0
        while k != 1:
            k = 1
            i = 0
            while i < len(s) - 1:
                if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                    s = s[:i] + s[i + 2:]
                    k += 1
                else:
                    i += 1
        return s