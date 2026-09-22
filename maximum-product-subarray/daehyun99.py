# Time: O(N)
# Space: O(N)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        zero_idx = set([i for i in range(len(nums)) if nums[i] == 0])
        prefix = [0 for _ in  range(len(nums))]
        suffix = [0 for _ in  range(len(nums))]

        val = 1
        for i in range(len(nums)):
            if i in zero_idx:
                val = 1
                continue
            else:
                val *= nums[i]
                prefix[i] = val
        val = 1
        for i in range(len(nums)-1, -1, -1):
            if i in zero_idx:
                val = 1
                continue
            else:
                val *= nums[i]
                suffix[i] = val
        return max(max(prefix), max(suffix))
