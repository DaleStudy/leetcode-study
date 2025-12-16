from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for num in nums[1:]:
            if num>dp[-1]:
                dp.append(num)
            else:
                dp[bisect_left(dp, num)] = num

        return len(dp)
    
