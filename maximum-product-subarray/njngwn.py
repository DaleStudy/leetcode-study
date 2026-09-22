class Solution:
    # Time Complexity: O(n), n: nums.length
    # Space Complexity: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        prefix, suffix = 1, 1

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n-1-i] * (suffix or 1)
            res = max(res, max(prefix, suffix))

        return res
