class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 시간복잡도: O(n) - nums 배열을 한 번만 순회함
        # 공간복잡도: O(n) - dp 배열을 nums 길이만큼 생성
        
        # DP
        dp = [0]*len(nums)
        dp[0] = nums[0]         # 초기화

        for i in range(1,len(nums)):
            # 현재값과 (이전까지의 합 + 현재값) 중 더 큰 값을 dp[i]에 저장 
            dp[i] = max(nums[i], nums[i]+dp[i-1])  

        return max(dp)
