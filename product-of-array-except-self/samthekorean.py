# TC : O(n)
# SC : O(1)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans
