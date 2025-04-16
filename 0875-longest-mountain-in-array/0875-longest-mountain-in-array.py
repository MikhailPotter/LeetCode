class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        length = 0
        cur_length = 1
        up = False
        down = False

        l = 0
        r = 1
        while r < len(arr):
            while r < len(arr) and arr[r] > arr[l]:
                r += 1
                l += 1
                cur_length += 1
                up = True
            while r < len(arr) and arr[r] < arr[l]:
                r += 1
                l += 1
                cur_length += 1
                down = True
            
            if cur_length > length and up and down:
                length = cur_length
            
            while r < len(arr) and arr[l] == arr[r]:
                r += 1
                l += 1
            
            cur_length = 1
            up = False
            down = False

        return length 
        