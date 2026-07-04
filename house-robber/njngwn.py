class Solution:
    # Time Complexity: O(n), n: len(nums)
    # Space Complextiy: O(1)
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        two_ago = nums[0]
        one_ago = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            current = max(one_ago, two_ago + nums[i])
            two_ago, one_ago = one_ago, current

        return one_ago
