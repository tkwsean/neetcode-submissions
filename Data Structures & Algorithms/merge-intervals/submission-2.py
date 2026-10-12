class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # merge based on start
        intervals.sort(key = lambda x: x[0])
        prevInterval = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            currInterval = intervals[i]
            if currInterval[0] <= prevInterval[1]:
                maxEnd = max(currInterval[1], prevInterval[1])
                prevInterval[1] = maxEnd
            else:
                result.append(prevInterval)
                prevInterval = currInterval
        result.append(prevInterval)
        return result

                
