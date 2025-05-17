import bisect

class Solution:
    def lengthOfLIS(self, nums):
        subsequence = []
        
        for num in nums:
            idx = bisect.bisect_left(subsequence, num)
            
            if idx == len(subsequence):
                subsequence.append(num)
            else:
                subsequence[idx] = num
        
        return len(subsequence)
