# TC: O(N)
# SC: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2

        for num in nums:
            total -= num

        return total

