class Solution:
    def rob(self, nums: List[int]) -> int:
        prevOne, prevTwo = 0, 0
        for num in nums:
            tmp = max(prevTwo+num, prevOne)
            prevTwo = prevOne
            prevOne = tmp
        return prevOne