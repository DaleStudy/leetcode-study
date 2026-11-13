class Solution:
    def rob(self, nums: list[int]) -> int:
        #시간, 공간 복잡도: O(n)
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)
        dp=nums.copy() # dp[i] = i번째 집의 money를 훔칠 때의 최대 누적 금액
        for i in range(2,len(nums)):
            house3 = dp[i-3] if i >= 3 else 0 #i=2일 경우에는 i-3이 존재하지 않기에 따로 처리
            dp[i] += max(dp[i-2], house3) #인접한 집은 방문 불가
        return max(dp)
        
