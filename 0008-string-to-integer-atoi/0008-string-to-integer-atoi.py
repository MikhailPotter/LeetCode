class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sgn = 1
        if s[0] == '-':
            sgn = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        res = 0
        for i, symbol in enumerate(s):
            if symbol.isdigit():
                res *= 10
                res += int(symbol)
            else:
                break   
        res *= sgn
        INT_MAX=2 ** 31-1
        INT_MIN=-2 ** 31
        if res > INT_MAX: 
            res = INT_MAX
        elif res < INT_MIN:  
            res = INT_MIN
        return res
    