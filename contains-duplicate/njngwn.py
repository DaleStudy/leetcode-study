class Solution:
    # Time Complexity: O(nlogn), n: len(nums)
    # Space Complexity: O(1)
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # O(nlogn)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                return True

        return False
