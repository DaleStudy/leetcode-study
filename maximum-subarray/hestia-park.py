class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = 0
        max_ = float('-inf')
        for i in range(len(nums)):
            dp += nums[i]
            max_ = max(max_, dp)
            if dp < 0:
                dp = 0  # 누적합이 0보다 작아지면 버리고 새로 시작
        return max_


