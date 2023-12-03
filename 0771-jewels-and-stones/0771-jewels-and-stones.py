class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0 
        for i in range(len(stones)):
            if stones[i] in jewels:
                res += 1
        return res