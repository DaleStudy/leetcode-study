# TC: O(N)
# SC: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        m, idx = 0, 0

        while idx <= m and idx < n:
            m = max(m, idx + nums[idx])
            idx += 1

        return m >= n - 1

