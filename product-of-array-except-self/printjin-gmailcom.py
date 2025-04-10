class Solution:
    def productExceptSelf(self, nums):
        ans = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]
            ans.append(product)
        return ans