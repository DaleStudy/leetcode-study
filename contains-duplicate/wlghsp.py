"""
 * Time Complexity: O(N)
 * Space Complexity: O(N)
"""
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
