class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            for j in range(len(s), min(i + len(res), len(s) - len(res)) - 1, -1):
                string = s[i:j + 1]
                if len(string) > len(res) and string == string[::-1]:
                    res = string
        return res