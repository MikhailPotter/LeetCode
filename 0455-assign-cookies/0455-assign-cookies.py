class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        
        res = 0
        for ck in s:
            print(ck, res, g[res])
            if ck >= g[res]:
                res += 1
                if res == len(g):
                    return res
        return res