class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo for DP
        dp = {}
        return self.robs(nums, dp, len(nums) - 1)

    def robs(self, nums: List[int], dp: Dict[int, int], houseToRob: int) -> int:
        if houseToRob < 0:
            return 0
        
        if houseToRob - 2 not in dp:
            dp[houseToRob - 2] = self.robs(nums, dp, houseToRob - 2)
        
        if houseToRob - 1 not in dp:
            dp[houseToRob - 1] = self.robs(nums, dp, houseToRob - 1)


        return max(
            dp[houseToRob - 2] + nums[houseToRob],
            dp[houseToRob - 1]    
        )
