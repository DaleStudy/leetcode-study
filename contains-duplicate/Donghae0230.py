class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        list_nums = list(set_nums)
        if len(nums) != len(list_nums):
            return True
        else:
            return False
