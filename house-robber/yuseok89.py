// TC: O(n), SC: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:

        two_before, one_before = 0, 0

        for num in nums:
            cur = max(two_before + num, one_before)
            two_before = one_before
            one_before = cur

        return max(one_before, two_before)

