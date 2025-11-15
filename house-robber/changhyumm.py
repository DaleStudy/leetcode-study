class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # 집이 하나면 최대 profit은 그 자체
        if n == 1:
            return nums[0]
        
        # dp[i]를 i+1 집까지 털었을때의 max라고 정의
        # dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # dp를 누적
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            
        # time O(n) - loop 1번
        # space O(n) - dp 배열 
        return dp[-1]
