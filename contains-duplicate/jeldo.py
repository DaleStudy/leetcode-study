class Solution:
    # O(n)
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))  # O(n)
