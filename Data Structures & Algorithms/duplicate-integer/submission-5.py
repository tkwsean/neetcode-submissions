class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        specialSet = set()
        for i in range(len(nums)):
            if nums[i] in specialSet:
                return True
            specialSet.add(nums[i])
        return False