class NumArray:

    nums = []
    all_sum = 0
    ln = 0
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.all_sum = sum(nums)
        self.ln = len(nums)

    def update(self, index: int, val: int) -> None:
        self.all_sum += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        if right - left > self.ln // 2:
            ans = sum(self.nums[:left]) + sum(self.nums[right + 1:])
            return self.all_sum - ans
        else:
            return sum(self.nums[left: right + 1])   


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)