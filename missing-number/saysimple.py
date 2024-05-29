# TC: O(n), SC: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
