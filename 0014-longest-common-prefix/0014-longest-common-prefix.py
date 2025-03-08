class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ''
        for i in range(len(strs[0])+1):
            pref = strs[0][0:i]
            print(1, pref)
            for word in strs:
                if pref != word[0:len(pref)]:
                    print(2,pref)
                    return pref[:-1]
        print(3, pref)
        return pref