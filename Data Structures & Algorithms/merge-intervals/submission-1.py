class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort based on start
        intervals.sort(key=lambda element: element[0])
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append([intervals[i][0], intervals[i][1]])
        return res

                
