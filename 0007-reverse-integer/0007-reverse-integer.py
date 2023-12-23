class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x *= -1
            res = -1
        else:
            res = 1
        res *= int(str(x)[::-1])
        
        if (res < - 2 ** 31) or (res >= 2 ** 31):
            return 0
        return res