class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            key = " ".join(sorted(word))
            if key in ans:
                ans[key].append(word)
            else:
                ans[key] = [word]
        return ans.values()