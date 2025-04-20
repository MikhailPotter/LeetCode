class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        hm = {
            '}': '{',
            ')': '(',
            ']': '[',
        }

        for c in s:
            if stack and c in hm and hm[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        if stack:
            return False
        return True
        