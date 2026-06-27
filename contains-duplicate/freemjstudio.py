class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        first = len(nums)
        set_nums = set(nums)
        second = len(set_nums)
        return (first != second)