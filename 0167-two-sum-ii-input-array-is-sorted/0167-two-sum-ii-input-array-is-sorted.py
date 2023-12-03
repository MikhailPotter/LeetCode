class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = dict()
        for i in range(len(numbers)):
            if target - numbers[i] in s:
                return [s[target - numbers[i]] + 1, i + 1]
            s[numbers[i]] = i 