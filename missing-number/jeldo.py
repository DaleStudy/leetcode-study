class Solution:
    # O(n), n = len(nums)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)
