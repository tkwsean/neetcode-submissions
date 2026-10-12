class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1
        maxArea = 0
        while l < r:
            maxArea = max(maxArea, min(heights[l], heights[r])*(r-l))
            if heights[l] > heights[r]:
                r -= 1
                continue
            elif heights[r] > heights[l]:
                l += 1
                continue
            l += 1
            r -= 1
        return maxArea