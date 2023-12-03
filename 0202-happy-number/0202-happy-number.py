class Solution:
    def isHappy(self, n: int) -> bool:
        while n >= 10:
            cur = 0
            for j in range(len(str(n))):
                cur += int(str(n)[j])**2
            n = cur
        if n in [1,7]:
            return True
        return False