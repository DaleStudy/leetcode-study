class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        string_len = len(nums)
        set_len = len(set(nums))

        return string_len != set_len