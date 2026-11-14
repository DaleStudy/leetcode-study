"""
 * Time Complexity: O(N)
 * Space Complexity: O(N)
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for n in nums_set:
            if (n - 1) not in nums_set:
                length = 1
                while n + length in nums_set:
                    length += 1
                ans = max(length, ans)
        return ans
