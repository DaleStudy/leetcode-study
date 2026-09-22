# N is the length of array nums.
# TC: O(N) - stores elements in a hash set and performs O(1) lookups
# SC: O(N) - uses a hash set of size N


class Solution:

    def missingNumber(self, nums: list[int]) -> int:
        num_set = set(nums)

        for i in range(len(nums) + 1):
            if i not in num_set:
                return i

        return -1
