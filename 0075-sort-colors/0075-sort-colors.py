class Solution:
    def sortColors(self, nums: List[int]) -> None:

        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
                # print('red', end=': ')
            elif nums[white] == 1:
                white += 1
                # print('white', end=': ')
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
                # print('blue', end=': ')
            # print(nums)
        