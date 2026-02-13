# DP
# Time Complexity : O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # case 1: from start+1 to end
        p1, p2 = 0, 0
        for n in nums[1:]:
            val = max(p1 + n, p2)
            p1 = p2
            p2 = val
        case1 = p2

        # case 2: from start to end-1
        p1, p2 = 0, 0
        for n in nums[:-1]:
            val = max(p1 + n, p2)
            p1 = p2
            p2 = val
        case2 = p2

        return max(case1, case2)

