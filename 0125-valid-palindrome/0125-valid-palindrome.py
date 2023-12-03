class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = []
        for a in s:
            if a.isalpha():
                k.append(a.lower())
            elif a.isdigit():
                k.append(a)
        return k[::] == k[::-1]