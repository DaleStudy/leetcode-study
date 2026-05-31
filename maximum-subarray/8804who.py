class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        min_s = 0
        max_s = nums[0]

        for num in nums:
            s += num
            if max_s < s-min_s:
                max_s=s-min_s
            if min_s > s:
                min_s = s
        return max_s
    
