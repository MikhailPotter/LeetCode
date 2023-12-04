class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr = sorted(arr, reverse=True)
        for time in permutations(arr):
            if time[0] * 10 + time[1] < 24 and time[2] * 10 + time[3] < 60:
                return f"{time[0]}{time[1]}:{time[2]}{time[3]}"
        return ""
        