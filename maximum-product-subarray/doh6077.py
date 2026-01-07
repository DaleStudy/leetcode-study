#152. Maximum Product Subarray

# https://leetcode.com/problems/maximum-product-subarray/
# 


# Three cases to consider 
# negative number
# positive number
# zero - we reset the curMin and curMax to 1 ( neutral element for multiplication)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMin, curMax = 1, 1

        for num in nums:
            if num == 0 :
                curMin, curMax = 1, 1
                continue
            temp = curMax * num
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(curMin * num, temp, num)
            res = max(res, curMax)
        return res
        