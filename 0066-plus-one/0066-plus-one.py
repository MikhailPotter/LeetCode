class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits[-1] += 1
        while i != -1:
            if digits[i] < 10:
                break
            if i == 0 and digits[i] > 9:
                digits[0] %= 10
                digits.insert(0,1)
                break
            digits[i] = digits[i] % 10
            i -= 1
            digits[i] += 1
        return digits
        