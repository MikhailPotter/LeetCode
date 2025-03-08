class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        a = len(num1)
        b = len(num2)
        for i in range(a):
            for j in range(b):
                res += int(num1[a - 1 - i]) * int(num2[b - 1 - j]) * (10**(i + j))
        return str(res)