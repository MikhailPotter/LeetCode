class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if c == '}' and top != '{':
                    return False
                if c == ')' and top != '(':
                    return False
                if c == ']' and top != '[':
                    return False
                stack = stack[:-1]
        if stack:
            return False
        return True
        