class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr_sorted = sorted(arr)

        min_diff = -1
        for i in range(len(arr_sorted) - 1):
            if min_diff == -1 or arr_sorted[i+1] - arr_sorted[i] < min_diff:
                min_diff = arr_sorted[i+1] - arr_sorted[i]
        
        p = 0
        res = list()
        while p < len(arr_sorted) - 1:
            if arr_sorted[p+1] - arr_sorted[p] == min_diff:
                res.append([arr_sorted[p], arr_sorted[p+1]])
            p += 1
        
        return res