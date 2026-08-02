# hint 를 보고 해결.
# DP 로도 풀 수 있음.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []


        for num in nums:
            if len(seq) == 0:
                seq.append(num)
                continue

            i = 0
            
            while seq[i] < num:
                i = i + 1

                if i > len(seq) - 1:
                    break
            
            if i > len(seq) - 1:
                seq.append(num)
            else:
                seq[i] = num
    
        return len(seq)







# ------------

# TC : O(n^2)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        for i, num in enumerate(nums):

            max_val = 1

            for j in range(0, i):
                if nums[j] < num:
                    max_val = max(max_val, dp[j] + 1)
            
            dp[i] = max_val
        
        return max(dp)
    

# -----------

# TC : O(nlogn)
    
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        seq = []

        for i, num in enumerate(nums):
            if i == 0:
                seq.append(num)
                continue

            last = seq[len(seq) - 1] 
            if last < num:
                seq.append(num)
            elif last > num:
                target_idx = bisect_left(seq, num)
                seq[target_idx] = num
        
        return len(seq)
    
