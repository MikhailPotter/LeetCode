class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split()
        print(ss)
        dic = dict()
        if len(ss) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in dic:
                if dic[pattern[i]] != ss[i]:
                    return False
            elif ss[i] in dic.values():
                return False
            else:
                dic[pattern[i]] = ss[i]
        return True

        