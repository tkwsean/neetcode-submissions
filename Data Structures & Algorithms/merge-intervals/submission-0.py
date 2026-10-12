class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda startTime: startTime[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            endTime = res[-1][1]
            if start <= endTime:
                res[-1][1] = max(end, endTime)
            else:
                res.append([start, end])
        return res