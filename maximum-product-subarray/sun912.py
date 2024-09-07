"""
    TC: O(n)
    SC: O(1)
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minimum, maximum = 1, 1
        result = nums[0]

        for num in nums:
            minimum, maximum = min(minimum * num, maximum * num, num), max(minimum * num, maximum * num, num)
            result = max(maximum, result)

        return result

