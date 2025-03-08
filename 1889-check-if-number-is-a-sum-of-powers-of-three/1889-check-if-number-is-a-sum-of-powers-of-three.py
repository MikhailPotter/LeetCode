class Solution:
    import math 

    def checkPowersOfThree(self, n: int) -> bool:
        deg = 3 ** (int(math.log(n, 3)) + 1)
        while deg >= 1:
            if deg > n:
                deg //= 3
                continue
            if n // deg == 2:
                return False
            n -= deg
        return True