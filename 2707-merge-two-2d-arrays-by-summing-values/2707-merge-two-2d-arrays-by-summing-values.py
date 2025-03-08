class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dict_1 = {a: b for a, b in nums1}
        dict_2 = {a: b for a, b in nums2}
        return [
            [a, dict_1.get(a, 0) + dict_2.get(a, 0)]
            for a in sorted(set(dict_1.keys()) | set(dict_2.keys()))
        ]
