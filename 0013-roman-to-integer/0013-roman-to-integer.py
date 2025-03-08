class Solution:
    def romanToInt(self, s: str) -> int:
        val_d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500, 
            'M': 1000,
        }
        if len(s) == 1:
            return val_d[s]
        res = val_d[s[-1]]
        for i in range(0, len(s) - 2):
            if (val_d[s[i]] < val_d[s[i+1]]) or (val_d[s[i]] < val_d[s[i+2]]):
                res -= val_d[s[i]]
            else: 
                res += val_d[s[i]]
        if val_d[s[-2]] < val_d[s[-1]]:
            res -= val_d[s[-2]]
        else:
            res += val_d[s[-2]]
        return res
        