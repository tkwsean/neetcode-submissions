class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, furthest, res = 0, 0, 0, 0
        while r < len(nums) - 1:
            for i in range(l, r+1):
                furthest = max(furthest, nums[i]+i)
            l = r+1
            r = furthest
            res += 1
        return res