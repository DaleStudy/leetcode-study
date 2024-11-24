from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max_sum = nums[0]
        local_max_sum = nums[0]
        
        for num in nums[1:]:
            local_max_sum = max(num, local_max_sum + num)
            global_max_sum = max(global_max_sum, local_max_sum)

        return global_max_sum
