class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        i = len(nums) // 2
        j = (len(nums) - 1) // 2
        return (nums[i] + nums[j]) / 2