class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        words_rev = {word[::-1]: i for i, word in enumerate(words)}

        for i, word in enumerate(words):
            if "" in words_rev and words_rev[""] != i and word == word[::-1]:
                ans.append([i, words_rev[""]])

            for j in range(1, len(word) + 1):
                l = word[:j]
                r = word[j:]
                if l in words_rev and words_rev[l] != i and r == r[::-1]:
                    ans.append([i, words_rev[l]])
                if r in words_rev and words_rev[r] != i and l == l[::-1]:
                    ans.append([words_rev[r], i])

        return ans
