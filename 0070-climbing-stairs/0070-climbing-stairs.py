class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        ways = [0] * n
        ways[0] = 1
        ways[1] = 2

        for i in range(2, n):
            ways[i] = ways[i-1] + ways[i-2]
        
        return ways[n-1]

        