class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for i in accounts:
            curr = 0
            for j in range(len(i)):
                curr += i[j]
            if max < curr:
                max = curr
        return max