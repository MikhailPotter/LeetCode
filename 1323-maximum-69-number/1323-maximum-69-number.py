class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        c = s.find('6')
        if c == -1:
            return int(s)
        return int(s[:c] + '9' + s[c + 1:])