class Solution:
    def countGoodNumbers(self, n: int) -> int:
        ans = 1
        ans = pow(20, n//2, 10**9 + 7)
        if n % 2 == 1:
            ans *= 5
        return ans % (10**9 + 7)
        