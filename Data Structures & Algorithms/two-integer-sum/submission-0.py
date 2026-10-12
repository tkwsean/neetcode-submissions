class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in dictionary:
                return [dictionary[complement], i]
            dictionary[nums[i]] = i
        return []