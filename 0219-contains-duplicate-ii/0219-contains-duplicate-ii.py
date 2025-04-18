class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = nums[:k+1]
        unique = set(window)

        if len(unique) != len(window):
            return True

        for i in range(k+1, len(nums)):
            remove_element = window.pop(0)
            unique.remove(remove_element)
            window.append(nums[i])
            unique.add(nums[i])
            if len(unique) != len(window):
                return True

        return False
