class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        special_set = set()
        for num in nums:
            if num in special_set:
                return num
            else:
                special_set.add(num)
        return -1