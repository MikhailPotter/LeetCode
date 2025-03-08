class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda row: row[0])
        fin_list = [intervals[0]]
        for i in range(len(intervals)):
            if fin_list[-1][-1] >= intervals[i][0] and fin_list[-1][-1] <= intervals[i][1]:
                fin_list[-1][-1] = intervals[i][1]
            elif fin_list[-1][-1] <= intervals[i][0]:
                fin_list.append(intervals[i])
        return fin_list