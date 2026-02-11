class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0]+nums
        dp1 = [0 for _ in range(len(nums))]
        dp2 = [0 for _ in range(len(nums))]

        dp1[1] = nums[1]

        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
        for i in range(2, len(nums)):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])

        return max(max(dp1), max(dp2))
    
