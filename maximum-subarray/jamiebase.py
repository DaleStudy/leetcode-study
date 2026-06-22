"""
# Intuition
max(전 위치까지의 sum + 지금 위치 값, 지금 위치의 값)

# Complexity
- Time complexity: nums의 길이를 N이라고 할 때 O(N)

- Space complexity: O(1)
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = nums[0]
        best = a
        for i in range(1, len(nums)):
            a = max(a + nums[i], nums[i])
            best = max(a, best)
        return best
