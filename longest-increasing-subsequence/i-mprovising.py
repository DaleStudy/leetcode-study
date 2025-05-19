"""
Time complexity O(n^2)
Space complexity O(n)

Dynamic programming
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [(1, nums[0])] # sequence len, max num in sequence

        for i in range(1, len(nums)):
            num = nums[i]
            max_len = 1
            for j in range(i):
                x, y = dp[j]
                if y < num:
                    if max_len < x + 1:
                        max_len = x + 1
            dp.append((max_len, num))

        # find max len
        max_len = 0
        for x in dp:
            if x[0] > max_len:
                max_len = x[0]

        return max_len
