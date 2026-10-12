class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        special_set = set()
        for i in range(len(nums)):
            if nums[i] in special_set:
                return True
            special_set.add(nums[i])
        return False