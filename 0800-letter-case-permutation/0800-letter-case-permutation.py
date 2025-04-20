class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def rec(cur, i):
            if len(s) == len(cur):
                res.append(cur)
                return 
            if s[i].isalpha():
                rec(cur + s[i].lower(), i + 1)
                rec(cur + s[i].upper(), i + 1)
            else:
                rec(cur + s[i], i + 1)
        
        res = list()
        rec('', 0)
        return res









        