class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        specialSet = set()
        for num in nums:
            if num in specialSet:
                return num
            specialSet.add(num)
        return -1