class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == -1:
            return 1 / x
        elif n == 1:
            return x
        elif n == 0:
            return 1
        if n % 2 == 0:
            return pow(x**2, n // 2)
        return x * pow(x**2, (n - 1) // 2)
        