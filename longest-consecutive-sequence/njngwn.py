class Solution:
    # Time Complexity: O(nlogn), n: len(nums)
    # Space Complexity: O(n), n: len(nums)
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums)) # O(nlogn)
        longest = 1
        length = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                length += 1
                longest = max(longest, length)
            else:
                length = 1

        return longest
