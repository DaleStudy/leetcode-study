class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        return int(n * (n + 1) / 2 - sum(nums))

        # TC: O(n), SC: O(1)
        # this only works for "only missing number", if there are multiple missing numbers, this won't work
