# 최대 부분 배열 합 문제

# O(n^2) time, O(1) space
# Time Limit Exceeded

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = nums[0]
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                max_total = max(total, max_total)
        return max_total
    
# 개선 풀이
# O(n) time, O(1) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = nums[0]
        total = nums[0]
        for i in range(1, len(nums)):
            total = max(nums[i], total + nums[i])
            max_total = max(total, max_total)
        return max_total 

# DP 풀이
# O(n) time, O(n) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)
