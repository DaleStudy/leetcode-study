class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numSet = set(nums)

        if (len(numSet) == len(nums)):
            return False

        return True
    