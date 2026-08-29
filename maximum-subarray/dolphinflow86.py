# 1) First of all, I tried to come up with a solution for a while but failed eventually.
# I got some hints from AI and then it was Kadane's algorithm. Calculate accumulated sum while iterating
# compare with the current number, if the current number is greater than accumulated sum + current number
# # reset accoumulted sum with current number. Otherwise update with new sum. 
# TC: O(N) where N is the size of the nums array
# SC: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        prev_sum = nums[0]
        max_sum = prev_sum
        for i in range(1, n):
            prev_sum = max(prev_sum + nums[i], nums[i])
            max_sum = max(max_sum, prev_sum)
        return max_sum
