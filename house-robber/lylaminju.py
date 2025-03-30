from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # prev1: 이전 집까지의 최대 이익
        # prev2: 전전 집까지의 최대 이익
        prev1, prev2 = 0, 0
        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1) # 현재 집을 털었을 때와 안 털었을 때 중 더 큰 이익 선택
            prev2 = temp
        
        return prev1
