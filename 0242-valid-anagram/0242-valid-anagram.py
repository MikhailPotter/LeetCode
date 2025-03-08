class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for n in set(s+t):
            if s.count(n) != t.count(n):
                return False
        return True