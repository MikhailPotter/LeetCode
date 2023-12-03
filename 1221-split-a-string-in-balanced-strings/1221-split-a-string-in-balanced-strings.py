class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        for i in range(len(s)):
            if s[i] == 'R':
                r += 1
            else:
                l += 1
            if r == l:
                res += 1
                r = 0
                l = 0 
        return res