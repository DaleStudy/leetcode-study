# idea: DP Top-down / Bottom-up
# DP was comp up on my head, but it is not easy for me to utilse recursive function. 


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]

        lst = [0]*length 
        lst[0] = nums[0]
        lst[1] = max(nums[0], nums[1])

        for i in range(2, length):
            lst[i] = max(lst[i-1], lst[i-2] + nums[i])

        return lst[-1]