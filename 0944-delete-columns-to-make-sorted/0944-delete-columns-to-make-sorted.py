class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            current = strs[0][i]
            for j in range(1, len(strs)):
                if current[-1] > strs[j][i]:
                    count += 1
                    break
                current += strs[j][i]
        return count        
        