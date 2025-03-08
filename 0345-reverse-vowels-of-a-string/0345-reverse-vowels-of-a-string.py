class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        l = 0
        r = len(s) - 1
        if not any(char in vowels for char in s):
            return s
        while r != l and l < r:
            if s[l] in vowels and s[r] in vowels:
                s = s[:l] + s[r] + s[l+1:r] + s[l] + s[r+1:]
                l += 1
                r -= 1
            while s[l] not in vowels:
                l += 1
            while s[r] not in vowels:
                r -= 1
        return s