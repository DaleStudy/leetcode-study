class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        prv = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    if dp[i] + 1 > dp[j]: 
                        dp[j] = dp[i] + 1
        """
        prv [-1, -1, -1,  2, 2, 3, 5,    5]
        dp  [ 1,  1,  1,  2, 2, 3, 4,    4]
        nums[10,  9,  2,  5, 3, 7, 101, 18]
        nums[2] = 2
        nums[4] = 3
        nums[5] = 7

                #dp[j] = max(dp[i] + 1, dp[j]) 
                # dp[i] + 1 <= dp[j]일 때 dp[j] 갱신X
                # LIS길이가 더 적거나 같은 상황. => LIS배열이 업데이트X
        """
        return max(dp)
    