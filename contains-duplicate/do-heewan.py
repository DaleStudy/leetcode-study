class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets = set(nums)

        if len(nums) != len(sets):
            return True
        return False

