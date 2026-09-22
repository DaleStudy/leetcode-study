# Time: O(N**2)
# Space: O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        counts = [1 for i in nums]

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    counts[i] = max(counts[i], counts[j]+1)
        return max(counts)
