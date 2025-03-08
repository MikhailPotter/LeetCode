class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = dict()
        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 0
        res = sorted(a, key=lambda item: a[item], reverse=True)
        return res[:k]
