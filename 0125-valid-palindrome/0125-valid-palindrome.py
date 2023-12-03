class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ''
        for a in s:
            if a.isalpha():
                k += a.lower()
            elif a.isdigit():
                k += a
        return k[::] == k[::-1]