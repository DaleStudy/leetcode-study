'''
시간 복잡도: O(n)
공간 복잡도: O(n)
'''
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        dp_first = [0] * n
        dp_second = [0] * n

        dp_first[0], dp_first[1] = nums[0], max(nums[0], nums[1])
        dp_second[1], dp_second[2] = nums[1], max(nums[1], nums[2])

        for i in range(2, n):
            dp_first[i] = max(dp_first[i - 1], dp_first[i - 2] + nums[i])
            dp_second[i] = max(dp_second[i - 1], dp_second[i - 2] + nums[i])
        
        return max(dp_first[-2], dp_second[-1])
